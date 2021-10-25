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
        
    def init_event_handler(self):
        self.sio.on('connect', self.connect)
        self.sio.on('disconnect', self.disconnect)
        self.sio.on('server response', self.print_response)
        
    async def connect(self):
        print('connection established')

    async def disconnect(self):
        print('disconnected from server')
        
    async def print_response(self, data):
        print('Server response with data: ',data)
    
    async def run_client(self):
        await self.sio.connect(host + ':' + str(port))
        await self.sio.emit('client message', {'message': 'Hello I\'m client'})
        await self.sio.wait()
        
host = 'http://127.0.0.1'
port = 26100
socket_client = SocketClient(host, port)
asyncio.run(socket_client.run_client())

