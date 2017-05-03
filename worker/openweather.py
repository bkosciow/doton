from service.openweather import Openweather
from worker.worker import Worker


class OpenweatherWorker(Worker):
    """Openweather worker"""
    def __init__(self, apikey, widget):
        self.cities = {
            3103402: 'Bielsko-Biała'
        }
        self.widget = widget
        self.handler = Openweather(self.cities, apikey)

    def start(self):
        """start worker"""
        self.handler.start()

    def shutdown(self):
        """shudown worker"""
        self.handler.stop()

    def weather(self, city_id=None, key=None):
        """return curent weather"""
        if key is None:
            return self.handler.weather(city_id)
        return self.handler.weather(city_id)[key]

    def forecast(self, city_id=None, forecast_date=None):
        """return forecast"""
        return self.handler.forecast(city_id, forecast_date)

    def execute(self):
        """executes worker"""
        self.widget.change_values({
            'current': self.weather(),
            'forecast': self.forecast()
        })
