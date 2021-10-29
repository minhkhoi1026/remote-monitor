from pynput.keyboard import Listener

class KeyLogger:
    def __init__(self, on_key_press_listener = None):
        self.listener = None
        self.on_key_press_listener = on_key_press_listener

    def start(self):
        def on_press(key):
            key = str(key)
            if (key.startswith("Key.")): key = key[4:]
            else: key = key.strip('\'')   
            if (self.on_key_press_listener):
                self.on_key_press_listener(key)
            
        self.listener = Listener(on_press=on_press)
        self.listener.start()

    def stop(self):
        self.listener.stop()

if __name__ == "__main__":
    keylogger = KeyLogger()
    keylogger.start()
    import time
    time.sleep(50)
    keylogger.stop()

