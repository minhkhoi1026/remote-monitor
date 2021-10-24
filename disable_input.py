"""
source:https://stackoverflow.com/questions/29289945/how-to-temporarily-disable-keyboard-input-using-python/48093769
"""
import keyboard
import time
import ctypes
    
def lock_input():
    ctypes.windll.user32.BlockInput(True)
    
def unlock_input():
    ctypes.windll.user32.BlockInput(False)





