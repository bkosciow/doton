"""Used to get data from handlers and pass it to correct widget"""


class HandlerDispatcher(object):
    """class HandlerDispatcher"""
    def __init__(self, widgets):
        self.widgets = widgets

    def set_dht_data(self, node, temp, humi):
        """get gdata from DHT11 sensor"""
        if node in self.widgets:
            list(map(lambda item:item.change_values({
                'temp': temp,
                'humi': humi
            }), self.widgets[node]))

    def set_pir_data(self, node, movement):
        """get data from PIR sensor"""
        if node in self.widgets:
            list(map(lambda item: item.change_values({
                'pir': movement
            }), self.widgets[node]))

    def set_light_data(self, node, light):
        """get data from light detector"""
        if node in self.widgets:
            list(map(lambda item: item.change_values({
                'light': light
            }), self.widgets[node]))

    def set_relay_states(self, node, states):
        """get data from relay"""
        if node in self.widgets:
            list(map(lambda item: item.change_values({
                'states': states
            }), self.widgets[node]))
