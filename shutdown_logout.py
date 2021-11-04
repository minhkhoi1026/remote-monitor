import ctypes
import os

def logout():
    ctypes.windll.user32.ExitWindowsEx(0, 1)
    
def shutdown():
    os.system("shutdown -p -f")