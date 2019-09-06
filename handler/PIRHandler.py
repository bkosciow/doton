"""Handler for PIR sensor"""
from message_listener.abstract.handler_interface import \
    Handler as HandlerInterface


class PIRHandler(HandlerInterface):
    def handle(self, message):
        """Handle a message"""
        if message is not None and 'event' in message.data:
            if message.data['event'] == 'pir.movement':
                self.worker.set_pir_data(
                    message.data['node'],
                    True
                )

            if message.data['event'] == 'pir.nomovement':
                self.worker.set_pir_data(
                    message.data['node'],
                    False
                )
