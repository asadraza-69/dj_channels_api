import asyncio

from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer


class MyAsyncConsumer(AsyncConsumer):
    # This handler is called when the client initially opens a connection
    # and is about to finish the WebSocket handshake.
    async def websocket_connect(self, event):
        print('WebSocket Connect...')
        await self.send({
            'type': 'websocket.accept',
            'accept': True,
        })

    # This handler is called when data is received from the client.
    async def websocket_receive(self, event):
        print('Message received from Client', event)
        print('Message received from Client', event['text'])
        for i in range(50):
            await self.send(dict(type='websocket.send', text=f'Hello World = {i}'))

            await asyncio.sleep(1)

    # This handler is called when the connection to the client is lost,
    # either from the client closing the connection or other reasons.
    async def websocket_disconnect(self, event):
        print('Websocket Disconnect...')
        raise StopConsumer
