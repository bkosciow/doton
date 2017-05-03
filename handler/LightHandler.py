"""Handler for light sensor"""
from message_listener.abstract.handler_interface import \
    Handler as HandlerInterface


class LightHandler(HandlerInterface):
    def handle(self, message):
        """handle a message"""
        if message is not None and 'event' in message:
            if message['event'] == 'detect.light':
                self.worker.set_light_data(
                    message['node'],
                    True
                )

            if message['event'] == 'detect.dark':
                self.worker.set_light_data(
                    message['node'],
                    False
                )
