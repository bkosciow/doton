"""Openweathermap service"""
import time
import threading
import urllib.error
import urllib.request
import json
import datetime
from service.openweather_codes import CODES
import socket


class Openweather(threading.Thread):
    """Openweather class to get data from openweathermap"""
    def __init__(self, cities, apikey):
        threading.Thread.__init__(self)
        self.cities = cities
        self.work = True
        self.tick = {'sleep': 10, 'weather_counter': 6*10, 'forecast_counter': 6*60}
        self.tick['_wcounter'] = self.tick['weather_counter'] + 1
        self.tick['_fcounter'] = self.tick['forecast_counter'] + 1

        self.weather_row_stub = {
            'update': 0,
            'temperature_min': 0,
            'temperature_max': 0,
            'temperature_current': 0,
            'humidity': 0,
            'pressure': 0,
            'wind_speed': 0,
            'wind_deg': 0,
            'clouds': 0,
            'weather_id': 0,
            'weather': ''
        }
        self.current_weather_raw = {i: "" for i in cities}
        self.current_weather = {i: self.weather_row_stub.copy() for i in cities}

        self.forecast_weather_raw = {i: {} for i in cities}
        self.forecast_weather = {i: {} for i in cities}

        self.url_current = "http://api.openweathermap.org/data/2.5/weather?id=%CITY_ID%&units=metric&mode=json&APPID="+apikey
        self.url_forecast = "http://api.openweathermap.org/data/2.5/forecast/daily?id=%CITY_ID%&mode=json&units=metric&cnt=4&APPID="+apikey

    def run(self):
        """main loop, reads data from openweather server"""
        while self.work:
            if self.tick['_wcounter'] > self.tick['weather_counter']:
                for city_id in self.cities:
                    """current weather"""
                    url = self.url_current.replace("%CITY_ID%", str(city_id))
                    json_data = self._fetch_data(url)
                    if json_data:
                        self.current_weather_raw[city_id] = json_data
                        self._decode(city_id)
                        self.tick['_wcounter'] = 0

            if self.tick['_fcounter'] > self.tick['forecast_counter']:
                for city_id in self.cities:
                    """ forecast """
                    url = self.url_forecast.replace("%CITY_ID%", str(city_id))
                    json_data = self._fetch_data(url)
                    if json_data:
                        for row in json_data['list']:
                            date = (datetime.datetime.fromtimestamp(int(row['dt']))).strftime("%Y-%m-%d")
                            self.forecast_weather_raw[city_id][date] = row
                            self.forecast_weather[city_id][date] = self._decode_forecast(row)
                        self.tick['_fcounter'] = 0

            time.sleep(self.tick['sleep'])
            self.tick['_wcounter'] += 1
            self.tick['_fcounter'] += 1

    def stop(self):
        """stops a thread"""
        self.work = False

    def get_raw_data(self, city_id=None):
        """return raw weather data"""
        if city_id is None:
            return self.current_weather_raw.itervalues().next()
        else:
            return self.current_weather_raw[city_id]

    def weather(self, city_id=None):
        """return decoded weather"""
        if not city_id:
            city_id = list(self.cities.keys())[0]

        return self.current_weather[city_id]

    def forecast(self, city_id=None, date=None):
        """return forecast"""
        if not city_id:
            city_id = list(self.cities.keys())[0]
        if date is None:
            date = time.strftime("%Y-%m-%d", time.localtime(time.time() + 24*3600))

        if not date in self.forecast_weather[city_id]:
            return self.weather_row_stub

        return self.forecast_weather[city_id][date]

    def _fetch_data(self, url):
        """fetch json data from server"""
        try:
            request = urllib.request.Request(url, None, {'User-Agent': 'RaspberryPI / Doton'})
            response = urllib.request.urlopen(request)
            data = response.read()
            json_data = json.loads(data.decode())
        except urllib.error.URLError as e:
            json_data = None
            print(time.strftime("%Y-%m-%d %H:%M:%S"), "error fetching from url", url, "\nreason", e.reason)
        except socket.timeout as e:
            json_data = None
            print(time.strftime("%Y-%m-%d %H:%M:%S"), "time out error from url", url, "\nreason", e.reason)
        except ValueError as e:
            json_data = None
            print("Decode failed")

        return json_data

    def _decode(self, city_id):
        """decode raw readings"""
        self.current_weather[city_id] = {
            'temperature_current': self.current_weather_raw[city_id]['main']['temp'],
            'humidity': self.current_weather_raw[city_id]['main']['humidity'],
            'pressure': self.current_weather_raw[city_id]['main']['pressure'],
            'wind_speed': self.current_weather_raw[city_id]['wind']['speed'],
            'wind_deg': self.current_weather_raw[city_id]['wind']['deg'],
            'weather_id': self.current_weather_raw[city_id]['weather'][0]['id'],
            'weather': CODES[self.current_weather_raw[city_id]['weather'][0]['id']],
            'clouds': self.current_weather_raw[city_id]['clouds']['all'],
            'update': self.current_weather_raw[city_id]['dt']
        }

    def _decode_forecast(self, row):
        """decode raw readings"""
        return {
            'temperature_min': row['temp']['min'],
            'temperature_max': row['temp']['max'],
            'humidity': row['humidity'],
            'pressure': row['pressure'],
            'wind_speed': row['speed'],
            'wind_deg': row['deg'],
            'weather_id': row['weather'][0]['id'],
            'weather': CODES[row['weather'][0]['id']],
            'clouds': row['clouds']
        }