import os 
import win32ui
import win32gui
import win32api
import win32con
import win32com.shell.shell as shell
from PIL import Image
import pickle
from enum import Enum
import time
import string
from ctypes import windll
from win32com.shell import shell, shellcon
import socket
import struct

def get_document_path():
    return shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

class file_opcode(Enum):
    LISTDIR = 1
    COPYFILE = 2
    PASTEFILE = 3
    DELFILE = 4

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

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            file_info = {}
            file_info["Filename"] = letter + ":\\"
            stat = os.stat(file_info["Filename"])
            file_info["Last modified"] = time.strftime("%d/%m/%Y %H:%M", time.localtime(stat.st_mtime))
            file_info["Icon"] = pickle.dumps(get_icon(file_info["Filename"], "small"))
            file_info["Filetype"] = "<DIR>"
            file_info["Filesize"] = ""
            drives.append(file_info)
        bitmask >>= 1

    return drives

def get_list_dir(root_dir = None):
    # if root directory is None return list of drives in computer
    if root_dir is None:
        return get_drives()
    
    # if root directory is specific poath return list of file and folder
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
            file_info["Filesize"] = f'{stat.st_size}b'
        else:
            file_info["Filetype"] = "<DIR>"
            file_info["Filesize"] = ""
        files.append(file_info)
    
    return files

def get_parent_dir(path):
    if path is None:
        return None
    if os.path.dirname(path) == path:
        return None
    return os.path.dirname(path)

def get_file(path):
    data = None
    with open(path, 'rb') as f:
        data = f.read()
    return data

def save_file(file_content, path):
    # TODO: handle duplicate file
    with open(path, 'wb') as f:
        data = f.write(file_content)

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        
def recv_file(host, port, path, buf_size = 65536):
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(1)
    with sock:
        client,addr = sock.accept()

        # Use a socket.makefile() object to treat the socket as a file.
        # Then, readline() can be used to read the newline-terminated metadata.
        with client, client.makefile('rb') as clientfile:
            length = int(clientfile.readline())

            # Read the data in chunks so it can handle large files.
            with open(path,'wb') as f:
                while length:
                    chunk = min(length, buf_size)
                    data = clientfile.read(chunk)
                    if not data: break # socket closed
                    f.write(data)
                    length -= len(data)
                
def send_file(host, port, path, buf_size = 65536):
    if host == '0.0.0.0':
        host = '127.0.0.1'
    sock = socket.socket()
    sock.connect((host ,port))
    with sock,open(path,'rb') as f:
        sock.sendall(f'{os.path.getsize(path)}'.encode() + b'\n')

        # Send the file in chunks so large files can be handled.
        while True:
            data = f.read(buf_size)
            if not data: break
            sock.sendall(data)
