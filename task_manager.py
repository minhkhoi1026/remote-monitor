"""Source: https://www.thepythoncode.com/article/make-process-monitor-python"""

import psutil
from datetime import datetime
import pandas as pd
import time
import os

def get_processes_info():
    # the list the contain all process dictionaries
    processes = []
    
    for process in psutil.process_iter():
        # get all process info in one shot
        with process.oneshot():
            # get the process id
            pid = process.pid
            if pid == 0:
                # System Idle Process for Windows NT, useless to see anyways
                continue
            
            # get the name of the file executed
            name = process.name()
            
            # get the time the process was spawned
            try:
                create_time = datetime.fromtimestamp(process.create_time())
            except OSError:
                # system processes, using boot time instead
                create_time = datetime.fromtimestamp(psutil.boot_time())
                
            # get the number of CPU cores that can execute this process
            try:
                cores = len(process.cpu_affinity())
            except psutil.AccessDenied:
                cores = 0
            # get the CPU usage percentage
            cpu_usage = process.cpu_percent()