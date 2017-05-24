import json
from service.openweather import Openweather
from worker.worker import Worker
import datetime


class OpenweatherWorker(Worker):
    """Openweather worker"""
    def __init__(self, config, widget):
        self.config = config
        self.cities = self._parse_cities(json.loads(config['cities']))
        self.widget = widget
        self.handler = Openweather(self.cities, config['apikey'])

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
        data = {
            'current': self.weather(),
            'forecast': {}
        }
        date_now = datetime.datetime.now()
        for day in range(0, 5):
            date = date_now + datetime.timedelta(days=day)
            data['forecast'][day] = self.forecast(None, date.strftime("%Y-%m-%d"))

        self.widget.change_values(data)

    def _parse_cities(self, values):
        """convert key to int"""
        return {int(key): value for key, value in values.items()}

