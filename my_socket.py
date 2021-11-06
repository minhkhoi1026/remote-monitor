import pickle
import struct
import os

class socket_adapter:
    def __init__(self, conn):
        self.__conn = conn
        
    def send(self, data):
        msg = pickle.dumps(data)
        size = len(msg)
        self.__conn.sendall(struct.pack('>L', size) + msg)
        
    def recv(self, buf_size = 32678):
        # receive response from server
        # size of message
        payload_size = struct.calcsize('>L')
        packed_msg_size = self.__conn.recv(payload_size)
        if packed_msg_size == b'':
            return None

        data = b""
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        size = msg_size
        
        # message content
        while size > 0:
            data += self.__conn.recv(min(size, buf_size))
            size = msg_size - len(data)
        return pickle.loads(data)
    
    def send_file(self, path, buf_size = 65536):
        size = os.stat(path).st_size
        with self.__conn, open(path, 'rb') as f:
            self.__conn.send(struct.pack('>L', size))
            # Send the file in chunks so large files can be handled.
            while True:
                data = f.read(buf_size)
                if not data: break
                self.__conn.sendall(data)
        
    def recv_file(self, path, buf_size = 65536):
        payload_size = struct.calcsize('>L')
        packed_msg_size = self.__conn.recv(payload_size)
        if packed_msg_size == b'':
            return None

        data = b""
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        size = msg_size
        
        # Read the data in chunks so it can handle large files.
        with open(path,'wb') as f:
            while size > 0:
                data = self.__conn.recv(min(size, buf_size))
                f.write(data)
                size = msg_size - len(data)
    
    def close(self):
        self.__conn.close()