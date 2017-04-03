from message_listener.abstract.handler_interface import Handler as HandlerInterface


class DHTHandler(HandlerInterface):
    def handle(self, message):
        if message is not None and 'event' in message and message['event'] == 'dht.status':
                self.worker.set_dht_data(
                    message['node'],
                    str(message['parameters']['temp']),
                    str(message['parameters']['humi'])
                )


