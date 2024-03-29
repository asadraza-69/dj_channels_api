from channels.consumer import SyncConsumer,AsyncConsumer

class MySyncConsumer (SyncConsumer) :
    # This handler is called when client initially opens a
    # connection and is about to finish the WebSocket handshake.
    def websocket_connect(self, event):
        print('Websocket Connected...')
    # This handler is called when data received from client
    def websocket_receive(self, event):
        print('Messaged Received...')
        
    # This handler is called when either connection to the client is
    # lost, either from the client closing the connection, the server
    # closing the connegtion, or loss of the socket
    def websocket_disconnect(self, event):
        print('Websocket Disconnected...')



# AsyncConsumer will expect you to write async-capable code.app/consumers.py
class MyAsyncConsumer(AsyncConsumer):
    # This handler is called when client initially opens a
    # connection and is about to finish the WebSocket handshake.
    async def websocket_connect(self, event):
        print('WebSocket Connect...')
    
    # This handler is called when data received from client
    async def websocket_receive(self, event):
        print('Websocket Received...')
        
    # This handler is called when either connection to the client is
    # lost, either from the client closing the connection, the server
    # closing the connegtion, or loss of the socket
    async def websocket_disconnect(self, event):
        print('Websocket Disconnect...')