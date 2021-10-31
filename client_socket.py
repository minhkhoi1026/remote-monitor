import asyncio
import socketio
import time
import threading
from utils import stoppabe_thread

def create_socket_client():
    sio = socketio.Client()
    return sio

class SocketClient:
    def __init__(self):
        self.__keylogger = None
        self.sio = create_socket_client()
        self.lock = threading.Lock()
        self.init_event_handler()
        
    def set_on_return_key_listener(self, callback):
        self.on_return_key_listener = callback
        
    def init_event_handler(self):
        self.sio.on('connect', self.__connect_handler)
        self.sio.on('disconnect', self.__disconnect_handler)
        self.sio.on('return_mac', self.__return_mac_handler)
        self.sio.on('return_key', self.__return_key_handler)
        self.on_return_key_listener = None
        
    def __connect_handler(self):
        print('connection established')

    def __disconnect_handler(self):
        print('disconnected from server')
        
    def __return_mac_handler(self, data):
        return data
            
    def __return_key_handler(self, key):
        print(key)
        if (self.on_return_key_listener):
            self.on_return_key_listener(key)
            
    def __keyhook_loop(self):
        while not threading.current_thread().is_stopped():
            with self.lock:
                self.sio.emit('request_key')
            time.sleep(2)
            
    def request_mac(self):
        self.sio.emit('request_mac')
        
    def start_keyhook(self):
        if not self.__keylogger:
            self.__keylogger = stoppabe_thread(target = self.__keyhook_loop, daemon = True)
            self.__keylogger.start()
    
    def stop_keyhook(self):
        self.lock.acquire()
        if self.__keylogger:
            self.sio.emit('stop_key')
            self.__keylogger.stop()
            self.__keylogger = None
        self.lock.release()
        
    def logout(self):
        self.sio.emit("logout")
        
    def shutdown(self):
        self.sio.emit("shutdown")
        
    def control_input(self, is_lock = True):
        self.sio.emit("control_input", {"is_lock": int(is_lock)})

    def connect(self, host = '127.0.0.1', port = 26100):
        self.sio.connect('http://' + host + ':' + str(port))
        
host = '127.0.0.1'
port = 26100
socket_client = SocketClient()
socket_client.connect(host, port)
socket_client.shutdown()