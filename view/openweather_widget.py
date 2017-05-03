from view.widget import Widget
from PIL import Image


class OpenweatherWidget(Widget):
    """Openweathermap widget"""
    def __init__(self, fonts):
        self.fonts = fonts
        self.colours = {
            'background_current': (127, 127, 0),
            'background_forecast': (0, 127, 127),
            'digit_background': (0, 0, 0),
            'border': (244, 244, 244)
        }
        self.current_weather = {
            'current': {
                'pressure': 0,
                'temperature_current': 0,
                'humidity': 0,
                'wind_speed': 0,
                'clouds': 0,
                'weather_id': 0,
                'update': 0,
                'wind_deg': 0,
                'weather': ''
            },
            'previous': None
        }
        self.forecast_weather = {
            'current': {
                'pressure': 0,
                'clouds': 0,
                'temperature_max': 0,
                'wind_speed': 0,
                'wind_deg': 0,
                'temperature_min': 0,
                'weather_id': 0,
                'humidity': 0,
                'weather': ''
            },
            'previous': None
        }
        self.icon = {
            'temperature': Image.open('assets/image/thermometer.png'),
            'compass': Image.open('assets/image/compass.png')
        }
        self.initialized = False

    def draw_widget(self, lcd, coords):
        """draw a tiles"""
        self._draw_widget(lcd, 'current', coords[0][0], coords[0][1])
        self._draw_widget(lcd, 'forecast', coords[1][0], coords[1][1])
        self.draw_values(lcd, coords, True)
        self.initialized = True

    def _draw_widget(self, lcd, widget_type, pos_x, pos_y):
        """draw a tile"""
        lcd.background_color = self.colours['background_'+widget_type]
        lcd.fill_rect(pos_x, pos_y, pos_x + 105, pos_y + 105)
        lcd.transparency_color = (0, 0, 0)
        lcd.draw_image(pos_x + 92, pos_y + 7, self.icon['temperature'])
        lcd.color = self.colours['border']
        lcd.draw_rect(pos_x, pos_y, pos_x + 105, pos_y + 105)

    def draw_values(self, lcd, coords, force=False):
        """draw values"""
        self._draw_values(lcd, 'current', coords[0][0], coords[0][1], force)
        self._draw_values(lcd, 'forecast', coords[1][0], coords[1][1], force)

    def _draw_values(self, lcd, widget_type, pos_x, pos_y, force=False):
        """draw current values"""
        if widget_type == 'current':
            current = self._get_value(
                widget_type, 'current', 'temperature_current'
            )
            previous = self._get_value(
                widget_type, 'previous', 'temperature_current'
            )
            if force or previous is None or current != previous:
                self.draw_number(
                    lcd, pos_x+50, pos_y+5, self.fonts['15x28'], current, previous, 20
                )
        else:
            current = self._get_value(
                widget_type, 'current', 'temperature_max'
            )
            previous = self._get_value(
                widget_type, 'previous', 'temperature_max'
            )
            if force or previous is None or current != previous:
                self.draw_number(
                    lcd, pos_x+50, pos_y+5, self.fonts['15x28'], current, previous, 20
                )

        current = self._get_value(widget_type, 'current', 'wind_speed')
        previous = self._get_value(widget_type, 'previous', 'wind_speed')
        if force or previous is None or current != previous:
            self.draw_number(
                lcd, pos_x+45, pos_y+39, self.fonts['15x28'], current, previous, 20
            )

        current = self._degree_to_direction(
            self.current_weather['current']['wind_deg']
        )
        previous = None if self.current_weather['previous'] is None \
            else self._degree_to_direction(self.current_weather['previous']['wind_deg'])
        if force or previous is None or current != previous:
            lcd.background_color = self.colours['background_'+widget_type]
            lcd.fill_rect(pos_x+84, pos_y+44, pos_x+99, pos_y+65)
            lcd.transparency_color = ((255, 255, 255), (0, 0, 0))
            lcd.draw_image(
                pos_x + 84,
                pos_y + 44,
                self.icon['compass'].rotate(
                    -1 * self.current_weather['current']['wind_deg']
                )
            )

        current = self._get_value(widget_type, 'current', 'pressure', 4)
        previous = self._get_value(widget_type, 'previous', 'pressure', 4)
        if force or previous is None or current != previous:
            self.draw_number(
                lcd, pos_x+25, pos_y+72, self.fonts['15x28'], current, previous, 20
            )

    def _get_value(self, widget_type, key, value, precision=2):
        """get value"""
        if widget_type == 'current':
            return None if self.current_weather[key] is None \
                else str(round(self.current_weather[key][value])).rjust(precision, '0')
        elif widget_type == 'forecast':
            return None if self.forecast_weather[key] is None \
                else str(round(self.forecast_weather[key][value])).rjust(precision, '0')

    def _degree_to_direction(self, degree):
        """degree to direction"""
        if 348.75 <= degree or degree < 11.25:
            return 'N'
        elif 11.25 <= degree < 33.75:
            return 'NNE'
        elif 33.75 <= degree < 56.25:
            return 'NE'
        elif 56.25 <= degree < 78.75:
            return 'ENE'
        elif 78.75 <= degree < 101.25:
            return 'E'
        elif 101.25 <= degree < 123.75:
            return 'ESE'
        elif 123.75 <= degree < 146.25:
            return 'SE'
        elif 146.25 <= degree < 168.75:
            return 'SSE'
        elif 168.75 <= degree < 191.25:
            return 'S'
        elif 191.25 <= degree < 213.75:
            return 'SSW'
        elif 213.75 <= degree < 236.25:
            return 'SW'
        elif 236.25 <= degree < 258.75:
            return 'WSW'
        elif 258.75 <= degree < 281.25:
            return 'W'
        elif 281.25 <= degree < 303.75:
            return 'WNW'
        elif 303.75 <= degree < 326.25:
            return 'NW'
        elif 326.25 <= degree < 348.75:
            return 'NNW'

    def change_values(self, values):
        if not self.initialized:
            return
        if 'current' in values:
            self.current_weather['previous'] = self.current_weather['current']
            self.current_weather['current'] = values['current']

        if 'forecast' in values:
            self.forecast_weather['previous'] = self.forecast_weather['current']
            self.forecast_weather['current'] = values['forecast']
