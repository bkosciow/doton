"""Handler for PIR sensor"""
from message_listener.abstract.handler_interface import Handler as HandlerInterface


class PIRHandler(HandlerInterface):
    def handle(self, message):
        """Handle a message"""
        if message is not None and 'event' in message:
            if message['event'] == 'pir.movement':
                self.worker.set_pir_data(
                    message['node'],
                    True
                )

            if message['event'] == 'pir.nomovement':
                self.worker.set_pir_data(
                    message['node'],
                    False
                )
