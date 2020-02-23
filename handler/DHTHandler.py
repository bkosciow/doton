"""Handler for DHT11"""
from message_listener.abstract.handler_interface import \
    Handler as HandlerInterface


class DHTHandler(HandlerInterface):
    def handle(self, message):
        """handle a message"""
        if message is not None \
                and 'event' in message.data and message.data['event'] == 'dht.status':
                for w in self.workers:
                    w.set_dht_data(
                        message.data['node'],
                        str(message.data['parameters']['temp']) if len(message.data['parameters']) else str(message.data['response']['temp']),
                        str(message.data['parameters']['humi']) if len(message.data['parameters']) else str(message.data['response']['humi'])
                    )
