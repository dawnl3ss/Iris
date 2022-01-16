import sys
import threading
import time
sys.path.append("../")
from conn.sock_parser import sock_parser

# server-side
class async_query_message(threading.Thread):

    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.parser = sock_parser()

    def run(self) -> None:
        self.parser.bind_sock_query_message(self.port)
        self.parser.listen_sock_query_message()
        (client, (client_adress, client_port)) = self.parser.accept_sock_query_message()

        while True:
            client.sendall("test".encode())
            time.sleep(1)