from time import sleep

from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):
    # This handler is called when the client initially opens a connection
    # and is about to finish the WebSocket handshake.
    def websocket_connect(self, event):
        print('Websocket Connected...')
        self.send({
            'type': 'websocket.accept',
            'accept': True,
        })

    # This handler is called when data is received from the client.
    def websocket_receive(self, event):
        print('Messaged Received...', event.get('text'))
        print('--------------------------------')
        for i in range(50):
            self.send(dict(type='websocket.send', text=f'Hello World = {i}'))
            sleep(1)

    # This handler is called when the connection to the client is lost,
    # either from the client closing the connection or other reasons.
    def websocket_disconnect(self, event):
        print('Websocket Disconnected...')
        raise StopConsumer
