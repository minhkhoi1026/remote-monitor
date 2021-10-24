import ctypes

def logout():
    ctypes.windll.user32.ExitWindowsEx(0, 1)
    
def shutdown():
    ctypes.windll.user32.ExitWindowsEx(0x00000008, 0x00000000)