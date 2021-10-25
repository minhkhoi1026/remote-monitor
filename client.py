import asyncio
import socketio

def create_socket_client():
    sio = socketio.AsyncClient()
    return sio

class SocketClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sio = create_socket_client()
        self.init_event_handler()
        
    def set_on_receive_key_listener(self, callback):
        self.on_receive_key_listener = callback
        
    def init_event_handler(self):
        self.sio.on('connect', self.__connect_handler)
        self.sio.on('disconnect', self.__disconnect_handler)
        self.sio.on('receive_mac', self.__receive_mac_handler)
        self.on_receive_key_listener = None
        
    async def __connect_handler(self):
        print('connection established')

    async def __disconnect_handler(self):
        print('disconnected from server')
        
    async def __receive_mac_handler(self, data):
        print(data)
        if (self.on_receive_key_listener):
            self.on_receive_key_listener(data)
            
    async def request_mac(self):
        await self.sio.emit('request_mac')

    async def run_client(self):
        await self.sio.connect(host + ':' + str(port))
        await socket_client.request_mac()
        await self.sio.wait()
        
host = 'http://127.0.0.1'
port = 26100
socket_client = SocketClient(host, port)
asyncio.run(socket_client.run_client())
