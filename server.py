from aiohttp import web
import socketio
from socketio import server
from getmac import get_mac_address 

def create_socket_server():
    sio = socketio.AsyncServer()
    app = web.Application()
    sio.attach(app)
    
    return sio, app

class SocketServer:
    def __init__(self, host, port):
        self.sio, self.app = create_socket_server()
        self.host = host
        self.port = port
        self.init_event_handler()
        
    def init_event_handler(self):
        self.sio.on('connect', self.__connect_handler)
        self.sio.on('disconnect', self.__disconnect_handler)
        self.sio.on('request_mac', self.__request_mac_handler)
        
    def __connect_handler(self, sid, environ):
        print("connect ", sid)
        
    def __disconnect_handler(self, sid):
        print('disconnect ', sid)

    async def __request_mac_handler(self, sid):
        await self.sio.emit('receive_mac', str(get_mac_address()))
    
    def run_server(self):
        web.run_app(self.app, host = self.host, port = self.port)
    
HOST = '127.0.0.1'
PORT = 26100
server_socket = SocketServer(HOST, PORT)
server_socket.run_server()
