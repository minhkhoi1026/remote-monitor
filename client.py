import asyncio
import socketio
import time

def create_socket_client():
    sio = socketio.Client()
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
        self.sio.on('receive_key', self.__receive_key_handler)
        self.on_receive_key_listener = None
        
    def __connect_handler(self):
        print('connection established')

    def __disconnect_handler(self):
        print('disconnected from server')
        
    def __receive_mac_handler(self, data):
        return data
            
    def __receive_key_handler(self, key):
        print(key)
        if (self.on_receive_key_listener):
            self.on_receive_key_listener(key)
            
    def request_mac(self):
        self.sio.emit('request_mac')
        
    def start_keyhook(self):
        self.sio.emit('request_keyhook')

    def connect(self):
        self.sio.connect(self.host + ':' + str(self.port))
        
host = 'http://127.0.0.1'
port = 26100
socket_client = SocketClient(host, port)
socket_client.connect()
print(socket_client.request_mac())
