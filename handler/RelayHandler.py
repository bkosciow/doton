"""Handler for relay states"""
from message_listener.abstract.handler_interface import \
    Handler as HandlerInterface


class RelayHandler(HandlerInterface):
    def handle(self, message):
        """handle a message"""
        if message is not None and 'event' in message.data:
            if message.data['event'] == 'channels.response':
                for w in self.workers:
                    w.set_relay_states(
                        message.data['node'],
                        message.data['response']
                    )
