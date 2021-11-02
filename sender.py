from streaming import StreamingServer
import threading

host = StreamingServer('127.0.0.1', 9999)
th = threading.Thread(target=host.start_server, daemon = True);

th.start()

while input() != "q":
    continue

host.stop_server()