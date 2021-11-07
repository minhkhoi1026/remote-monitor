import pickle
import struct

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
    
    def close(self):
        self.__conn.close()