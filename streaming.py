import cv2
import pyautogui
import numpy as np

import socket
import pickle
import struct
import threading

class StreamingServer:
    """
    Class for the streaming server.

    Attributes
    ----------

    Private:

        __host : str
            host address of the listening server
        __port : int
            port on which the server is listening
        __used_slot : int
            boolean for implement only serve one client at a time
        __x_res : int
            the x resolution
        __y_res : int
            the y resolution
        __running : bool
            indicates if the server is already running or not
        __block : Lock
            a basic lock used for the synchronization of threads
        __server_socket : socket
            the main server socket
        __encoding_parameters : list
            a list of encoding parameters for OpenCV


    Methods
    -------

    Private:

        _configure : sets basic configurations
        __init_socket : method that binds the server socket to the host and port
        __server_listening: method that listens for new connections
        __client_connection : main method for processing the client streams

    Public:

        start_server : starts the server in a new thread
        stop_server : stops the server and closes all connections
    """

    def __init__(self, host, port, x_res=1024, y_res=576):
        """
        Creates a new instance of StreamingServer

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
        self.__x_res = x_res
        self.__y_res = y_res
        self.__used_slot = False;
        self.__block = threading.Lock()
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__init_socket() 
        self._configure()
    
    def __init_socket(self):
        """
        Binds the server socket to the given host and port
        """
        self.__server_socket.bind((self.__host, self.__port))

    def _configure(self):
        """
        Basic configuration function.
        """
        self.__encoding_parameters = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

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
            
    def _get_frame(self):
        """
        Gets the next screenshot.

        Returns
        -------

        frame : the next screenshot frame to be processed
        """
        screen = pyautogui.screenshot()
        frame = np.array(screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (self.__x_res, self.__y_res), interpolation=cv2.INTER_AREA)
        return frame

    def __client_connection(self, connection):
        """
        Main method for sending client streaming data.
        """
        while self.__used_slot:
            frame = self._get_frame()
            result, frame = cv2.imencode('.jpg', frame, self.__encoding_parameters)
            data = pickle.dumps(frame, 0)
            size = len(data)

            try:
                connection.sendall(struct.pack('>L', size) + data)
            except ConnectionResetError:
                self.__used_slot = False
            except ConnectionAbortedError:
                self.__used_slot = False
            except BrokenPipeError:
                self.__used_slot = False
                
    def start_server(self):
        """
        Starts the server if it is not running already.
        """
        if self.__running:
            print("Server is already running")
        else:
            self.__running = True
            server_thread = threading.Thread(target=self.__server_listening)
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
            
class StreamingClient:
    """
    Class for the streaming client.

    Attributes
    ----------

    Private:

        __host : str
            host address to connect to
        __port : int
            port to connect to
        __quit_key : chr
            key that has to be pressed to close connection (default = 'q')  
        __running : bool
            inicates if the client is already streaming or not
        __client_socket : socket
            the main client socket


    Methods
    -------

    Private:

        __client_streaming : main method for streaming the client data

    Protected:

        _get_frame : returns the frame to be sent to the server (overridden by child classes)
        _cleanup : cleans up all the resources and closes everything

    Public:

        start_stream : starts the client stream in a new thread
    """

    def __init__(self, host, port):
        """
        Creates a new instance of StreamingClient.

        Parameters
        ----------

        host : str
            host address to connect to
        port : int
            port to connect to
        """
        self.__host = host
        self.__port = port
        self.__running = False
        self.__quit_key = 'q'
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_stream(self):
        """
        Starts client stream if it is not already running.
        """

        if self.__running:
            print("Client is already streaming!")
        else:
            self.__running = True
            client_thread = threading.Thread(target=self.__client_streaming)
            client_thread.start()

    def stop_stream(self):
        """
        Stops client stream if running
        """
        if self.__running:
            self.__running = False
        else:
            print("Client not streaming!")
            
    def __clean(self):
        self.__client_socket.close()
        self.__running = False

    def __client_streaming(self):
        """
        Handles the individual server connections and processes their stream data.
        """
        payload_size = struct.calcsize('>L')
        data = b""

        self.__client_socket.connect((self.__host, self.__port));
        while self.__running:

            while len(data) < payload_size:
                received = self.__client_socket.recv(4096)
                if received == b'':
                    self.__running = False
                    break
                data += received

            if not self.__running:
                break

            packed_msg_size = data[:payload_size]
            data = data[payload_size:]

            msg_size = struct.unpack(">L", packed_msg_size)[0]

            while len(data) < msg_size:
                data += self.__client_socket.recv(4096)

            frame_data = data[:msg_size]
            data = data[msg_size:]

            frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            cv2.imshow(self.__host, frame)
            if cv2.waitKey(1) == ord(self.__quit_key):
                break
    
        self.__clean();
        