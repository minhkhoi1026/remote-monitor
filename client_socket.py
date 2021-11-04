import socket
import time
import threading
import struct
import pickle
from task_manager import process_opcode
from utils import stoppabe_thread
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
    
    def __keyhook_loop(self, logger):
        while not threading.current_thread().is_stopped():
            with self.__lock:
                data = self.__request('request_key')
                if data is None:
                    return
                logger.info(data) # write new data to file
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
            self.__client_socket.connect((host, port))
            self.running = True
            return True
        except ConnectionRefusedError:
            return False
    
    def request_mac(self):
        return self.__request('request_mac')
    
    def start_keyhook(self, filename):
        if not self.__keylogger:
            logger = create_file_logger(filename)
            self.__keylogger = stoppabe_thread(target = self.__keyhook_loop, 
                                               args=[logger], daemon = True)
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
    
    def paste_file(self, file_content, path):
        return self.__request("file_management", 
                            {"opcode": file_opcode.PASTEFILE, 
                            "file_content": file_content, 
                            "path": path})
    def copy_file(self, path):
        return self.__request("file_management", 
                            {"opcode": file_opcode.COPYFILE, "path": path})
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
    client.start_keyhook("keylog.txt")
    time.sleep(5)
    client.stop_keyhook()
        
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
    # client.paste_file(get_file("README.md"), "E:\\README.md")
    # with open("test.md", "wb") as f:
    #     f.write(client.copy_file("E:\\repo\\remote-monitor\\README.md"))
    # client.del_file("E:\\repo\\remote-monitor\\test.md")
    # files = client.request_listdir("E:\\")
    # for file in files["content"]:
    #     print(file["Filename"], file["Filetype"], file["Filesize"], file["Last modified"])
