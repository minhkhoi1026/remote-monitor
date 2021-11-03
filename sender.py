from streaming import StreamingServer
import threading

host = StreamingServer('127.0.0.1', 9999)
host.start_server()

while input() != "q":
    continue

host.stop_server()