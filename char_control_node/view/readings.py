from lcdmanager.widget.pane import Pane
from lcdmanager.widget.label import Label


class Readings(object):
    def __init__(self, lcdmanager):
        self.pane = Pane(0, 0, 'data_summary')
        self.pane.width = lcdmanager.width
        self.pane.height = lcdmanager.height

        label_temp = Label(0, 1)
        label_temp.label = "Temp:"
        self.pane.add_widget(label_temp)

        label_humi = Label(0, 2)
        label_humi.label = "Humi:"
        self.pane.add_widget(label_humi)

        label_kitchen = Label(5, 0)
        label_kitchen.label = "Kitchen"
        self.pane.add_widget(label_kitchen)

        myroom = Label(13, 0)
        myroom.label = "My room"
        self.pane.add_widget(myroom)

        self.pane.add_widget(Label(6, 1, 'kitchen_temp'))
        self.pane.get_widget('kitchen_temp').label = '--'
        self.pane.add_widget(Label(6, 2, 'kitchen_humi'))
        self.pane.get_widget('kitchen_humi').label = '--'
        self.pane.add_widget(Label(7, 3, 'kitchen_move'))
        self.pane.get_widget('kitchen_move').label = '-'
        self.pane.add_widget(Label(10, 3, 'kitchen_light'))
        self.pane.get_widget('kitchen_light').label = '-'

        self.pane.add_widget(Label(14, 1, 'my-room_temp'))
        self.pane.get_widget('my-room_temp').label = '--'
        self.pane.add_widget(Label(14, 2, 'my-room_humi'))
        self.pane.get_widget('my-room_humi').label = '--'
        self.pane.add_widget(Label(15, 3, 'my-room_move'))
        self.pane.get_widget('my-room_move').label = '-'
        self.pane.add_widget(Label(18, 3, 'my-room_light'))
        self.pane.get_widget('my-room_light').label = '-'

        lcdmanager.add_widget(self.pane)
        self.node_name = {
            'node-kitchen': 'kitchen',
            'node-my-room': 'my-room'
        }

    def set_dht_data(self, node, temp, humi):
        if node in self.node_name:
            self.pane.get_widget(self.node_name[node] + '_temp').label = temp
            self.pane.get_widget(self.node_name[node] + '_humi').label = humi

    def set_pir_data(self, node, status):
        if node in self.node_name:
            if status:
                self.pane.get_widget(self.node_name[node] + '_move').label = 'M'
            else:
                self.pane.get_widget(self.node_name[node] + '_move').label = ' '

    def set_light_data(self, node, status):
        if node in self.node_name:
            if status:
                self.pane.get_widget(self.node_name[node] + '_light').label = 'L'
            else:
                self.pane.get_widget(self.node_name[node] + '_light').label = ' '
