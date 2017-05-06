"""Handler for relay states"""
from message_listener.abstract.handler_interface import \
    Handler as HandlerInterface


class RelayHandler(HandlerInterface):
    def handle(self, message):
        """handle a message"""
        if message is not None and 'event' in message:
            if message['event'] == 'channel.state':
                self.worker.set_relay_states(
                    message['node'],
                    message['parameters']
                )
