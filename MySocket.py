from socket import socket
import pickle
import struct

BUF_SIZE = 16384
class MySocket(socket):
    def send(self, event, data):
        msg = pickle.dumps([event, data])
        size = len(msg)
        super().sendall(struct.pack('>L', size) + msg)
        
    def recv(self):
        # receive response from server
        # size of message
        payload_size = struct.calcsize('>L')
        packed_msg_size = super().recv(payload_size)
        if packed_msg_size == b'':
            return None

        data = b""
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        size = msg_size
        
        # message content
        while size > 0:
            data += self.__client_socket.recv(min(size, BUF_SIZE))
            size = msg_size - len(data)
        return pickle.loads(data)