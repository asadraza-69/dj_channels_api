from channels.consumer import SyncConsumer, AsyncConsumer


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
        print('Messaged Received...',event.get('text'))
        print('--------------------------------')

    # This handler is called when the connection to the client is lost,
    # either from the client closing the connection or other reasons.
    def websocket_disconnect(self, event):
        print('Websocket Disconnected...')


class MyAsyncConsumer(AsyncConsumer):
    # This handler is called when the client initially opens a connection
    # and is about to finish the WebSocket handshake.
    async def websocket_connect(self, event):
        print('WebSocket Connect...')

    # This handler is called when data is received from the client.
    async def websocket_receive(self, event):
        print('Websocket Received...')

    # This handler is called when the connection to the client is lost,
    # either from the client closing the connection or other reasons.
    async def websocket_disconnect(self, event):
        print('Websocket Disconnect...')
