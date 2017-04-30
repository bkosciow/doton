

class HandlerDispacher(object):
    def __init__(self, widgets):
        self.widgets = widgets

    def set_dht_data(self, node, temp, humi):
        if node in self.widgets:
            self.widgets[node].change_values({
                'temp': temp,
                'humi': humi
            })

    def set_pir_data(self, node, movement):
        if node in self.widgets:
            self.widgets[node].change_values({
                'pir': movement
            })

    def set_light_data(self, node, light):
        if node in self.widgets:
            self.widgets[node].change_values({
                'light': light
            })
