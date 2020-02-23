"""Handler for light sensor"""
from message_listener.abstract.handler_interface import \
    Handler as HandlerInterface


class LightHandler(HandlerInterface):
    def handle(self, message):
        """handle a message"""
        if message is not None and 'event' in message.data:
            if message.data['event'] == 'detect.light':
                for w in self.workers:
                    w.set_light_data(
                        message.data['node'],
                        True
                    )

            if message.data['event'] == 'detect.dark':
                for w in self.workers:
                    w.set_light_data(
                        message.data['node'],
                        False
                    )
