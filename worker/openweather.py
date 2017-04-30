from service.openweather import Openweather
 
 
class OpenweatherWorker(object):
    def __init__(self, apikey):
        self.cities = {
            3103402: 'Bielsko-Biała',
            2946447: 'Bonn'
        }
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
