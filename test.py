import os 
import win32ui
import win32gui
import win32api
import win32con
import win32com.shell.shell as shell
from PIL import Image
import pickle

def get_icon(PATH, size):
    SHGFI_ICON = 0x000000100
    SHGFI_ICONLOCATION = 0x000001000
    if size == "small":
        SHIL_SIZE = 0x00001
    elif size == "large":
        SHIL_SIZE = 0x00002
    else:
        raise TypeError(
            "Invalid argument for 'size'. Must be equal to 'small' or 'large'")

    ret, info = shell.SHGetFileInfo(
        PATH, 0, SHGFI_ICONLOCATION | SHGFI_ICON | SHIL_SIZE)
    hIcon, iIcon, dwAttr, name, typeName = info
    ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
    hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_x)
    hdc = hdc.CreateCompatibleDC()
    hdc.SelectObject(hbmp)
    hdc.DrawIcon((0, 0), hIcon)
    win32gui.DestroyIcon(hIcon)

    bmpinfo = hbmp.GetInfo()
    bmpstr = hbmp.GetBitmapBits(True)
    img = Image.frombuffer(
        "RGBA",
        (bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
        bmpstr, "raw", "BGRA", 0, 1
    )
    return img
import time

def get_list_dir(root_dir):
    files = []
    for file in os.listdir(root_dir):
        full_path = os.path.join(root_dir, file)
        file_info = {}
        stat = os.stat(full_path)
        
        file_info["Filename"] = file
        file_info["Last modified"] = time.strftime("%d/%m/%Y %H:%M", time.localtime(stat.st_mtime))
        file_info["Icon"] = pickle.dumps(get_icon(full_path, "small"))
        
        if (os.path.isfile(full_path)):
            file_info["Filetype"] = os.path.splitext(file)[1]
            if len(file_info["Filetype"]) > 0:
                file_info["Filetype"] = file_info["Filetype"][1:]
            file_info["Filesize"] = stat.st_size
        else:
            file_info["Filetype"] = "<DIR>"
            file_info["Filesize"] = ""
        files.append(file_info)
    
    return files

def get_parent_dir(path):
    return os.path.dirname(path)

start_time = time.time()
root_dir = '.\\'
files = get_list_dir(root_dir)
print("--- %s seconds ---" % (time.time() - start_time))
# for file in files:
#     print(file)
    
import sys
print(sys.getsizeof(files))
