from aiohttp import web
import socketio
from socketio import server

def create_socket_server():
    sio = socketio.AsyncServer()
    app = web.Application()
    sio.attach(app)
    
    @sio.event
    def connect(sid, environ):
        print("connect ", sid)

    @sio.on('client message')
    async def response_client(sid, data):
        print('message received with ', data)
        await sio.emit('server response', {'response': 'Hello I\'m server'})

    @sio.event
    def disconnect(sid):
        print('disconnect ', sid)
    
    return sio, app


class SocketServer:
    def __init__(self, host, port):
        self.sio, self.app = create_socket_server()
        self.host = host
        self.port = port
    
    def run_server(self):
        web.run_app(self.app, host = self.host, port = self.port)
    
HOST = '127.0.0.1'
PORT = 26100
server_socket = SocketServer(HOST, PORT)
server_socket.run_server()
