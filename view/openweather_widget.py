import math
from view.widget import Widget
from PIL import Image


class OpenweatherWidget(Widget):
    """Openweathermap widget"""
    def __init__(self, coords, lcd, fonts):
        self.current_widget_pos = coords[0]
        self.forecast_widget_pos = coords[1]
        self.lcd = lcd
        self.fonts = fonts
        self.colours = {
            'background_current': (127, 127, 0),
            'background_forecast': (0, 127, 127),
            'digit_background': (0, 0, 0),
            'border': (244, 244, 244)
        }
        self.current_weather = {
            'current': {'pressure': 1018, 'temperature_current': 11.56, 'humidity': 70, 'wind_speed': 9.3, 'clouds': 75, 'weather_id': 803, 'update': 1493631000, 'wind_deg': 70, 'weather': 'broken clouds'},
            'previous': None
        }
        self.forecast_weather = {
            'current': {'pressure': 975.42, 'clouds': 24, 'temperature_max': 17.09, 'wind_speed': 1.86, 'wind_deg': 82, 'temperature_min': 3.52, 'weather_id': 501, 'humidity': 72, 'weather': 'moderate rain'},
            'previous': None
        }
        self.icon = {
            'temperature': Image.open('assets/image/thermometer.png'),
            'compass': Image.open('assets/image/compass.png')
        }

    def draw_widget(self):
        """draw a tiles"""
        self._draw_widget('current', self.current_widget_pos[0], self.current_widget_pos[1])
        self._draw_widget('forecast', self.forecast_widget_pos[0], self.forecast_widget_pos[1])
        self.draw_values(True)

    def _draw_widget(self, widget_type, pos_x, pos_y):
        """draw a tile"""
        self.lcd.background_color = self.colours['background_'+widget_type]
        self.lcd.fill_rect(pos_x, pos_y, pos_x + 115, pos_y + 103)
        self.lcd.transparency_color = (0, 0, 0)
        self.lcd.draw_image(pos_x + 95, pos_y + 7, self.icon['temperature'])
        self.lcd.color = self.colours['border']
        self.lcd.draw_rect(pos_x, pos_y, pos_x + 115, pos_y + 103)

    def draw_values(self, force=False):
        """draw values"""
        self._draw_values('current', self.current_widget_pos[0], self.current_widget_pos[1], force)
        self._draw_values('forecast', self.forecast_widget_pos[0], self.forecast_widget_pos[1], force)

    def _draw_values(self, widget_type, pos_x, pos_y, force=False):
        """draw current values"""
        if widget_type == 'current':
            current = self._get_value(widget_type, 'current', 'temperature_current')
            previous = self._get_value(widget_type, 'previous', 'temperature_current')
            if force or previous is None or current != previous:
                self.draw_number(
                    pos_x+50, pos_y+5, self.fonts['15x28'], current, previous, 20
                )
        else:
            current = self._get_value(widget_type, 'current', 'temperature_max')
            previous = self._get_value(widget_type, 'previous', 'temperature_max')
            if force or previous is None or current != previous:
                self.draw_number(
                    pos_x+50, pos_y+5, self.fonts['15x28'], current, previous, 20
                )

        current = self._get_value(widget_type, 'current', 'wind_speed')
        previous = self._get_value(widget_type, 'previous', 'wind_speed')
        if force or previous is None or current != previous:
            self.draw_number(
                pos_x+50, pos_y+39, self.fonts['15x28'], current, previous, 20
            )

        current = self._degree_to_direction(self.current_weather['current']['wind_deg'])
        previous = None if self.current_weather['previous'] is None else self._degree_to_direction(self.current_weather['previous']['wind_deg'])
        if force or previous is None or current != previous:
            self.lcd.transparency_color = ((255, 255, 255), (0, 0, 0))
            self.lcd.draw_image(
                pos_x + 92,
                pos_y + 44,
                self.icon['compass'].rotate(-1 * self.current_weather['current']['wind_deg'])
            )

        current = self._get_value(widget_type, 'current', 'pressure', 4)
        previous = self._get_value(widget_type, 'previous', 'pressure', 4)
        if force or previous is None or current != previous:
            self.draw_number(
                pos_x+30, pos_y+72, self.fonts['15x28'], current, previous, 20
            )

    def _get_value(self, widget_type, key, value, precision=2):
        """get value"""
        if widget_type == 'current':
            return None if self.current_weather[key] is None else str(round(self.current_weather[key][value])).rjust(precision, '0')
        elif widget_type == 'forecast':
            return None if self.forecast_weather[key] is None else str(round(self.forecast_weather[key][value])).rjust(precision, '0')

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
        pass