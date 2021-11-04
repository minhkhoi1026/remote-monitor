import os
import subprocess
import ctypes
from ctypes import wintypes
import signal
from enum import Enum

class process_opcode(Enum):
    LISTPROC = 1
    STARTPROC = 2
    KILLPROC = 3
    LISTAPP = 4
    STARTAPP = 5

# argument type define for win api cross-platform func
WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL,
                                 wintypes.HWND,
                                 wintypes.LPARAM)
user32 = ctypes.windll.user32
user32.EnumWindows.argtypes = [
    WNDENUMPROC,
    wintypes.LPARAM]
user32.GetWindowTextLengthW.argtypes = [
    wintypes.HWND]
user32.GetWindowTextW.argtypes = [
    wintypes.HWND,
    wintypes.LPWSTR,
    ctypes.c_int]

app_pids = []

# callback for enumerate window
def EnumCallback(hwnd, lParam):
    # if window title length > 0 then the window is opening
    length = user32.GetWindowTextLengthW(hwnd)
    if (length > 0):
        pid = ctypes.c_ulong()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        app_pids.append(str(pid.value))
    return True

cb_worker = WNDENUMPROC(EnumCallback)

# parse lines info into dictionary
def parse_powershell(lines):
    res = []
    cur_item = {}
    for line in lines:
        tokens = [elem.strip() for elem in line.split(':')]
        if len(tokens) > 2:
            cur_item[tokens[0]] = ':'.join(tokens[1:])
        elif len(tokens) > 1:
            cur_item[tokens[0]] = tokens[1]
        else:
            if cur_item: res.append(cur_item)
            cur_item = {}
    return res

# return list of running process
def get_running_processes():
    # get data as string from power shell
    cmd = "powershell gps | select Name,@{Name='PID';Expression={$_.ID}},@{Name='Thread Count';Expression={$_.Threads.Count}} | fl"
    data = subprocess.check_output(cmd)
    
    # parse data to dict for return
    lines = str(data).split("\\r\\n")
    procs = parse_powershell(lines)
    
    # get list of process that has GUI
    app_pids.clear()
    user32.EnumWindows(cb_worker, 42)
    # add status of process for identify if process has GUI
    for proc in procs:
        proc["is_app"] = int(proc["PID"] in app_pids)
    return procs

# kill process by pid
def kill_process(pid):
    os.kill(pid, signal.SIGTERM)
    
# start process by name
def start_process(proc_name):
    subprocess.Popen(proc_name)
    
def get_installed_apps():
    # get data as string from power shell
    cmd = "powershell get-StartApps | fl"
    data = subprocess.check_output(cmd)
    
    # parse data to dict for return
    lines = str(data).split("\\r\\n")
    
    return parse_powershell(lines)

def start_app(app_id):
    subprocess.Popen(["powershell.exe", f"explorer shell:appsfolder\\{app_id}"])

if __name__ == '__main__':
    import time
    start_time = time.time()
    procs = get_running_processes()
    print("--- %s seconds ---" % (time.time() - start_time))
    # for proc in procs:
    #     if proc["is_app"]:
    #         print(proc)
    
    start_time = time.time()
    apps = get_installed_apps()
    print("--- %s seconds ---" % (time.time() - start_time))
    # for app in apps:
    #     print(app)
    # start_app(apps[0]['AppID'])