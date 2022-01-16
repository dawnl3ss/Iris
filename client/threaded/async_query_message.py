import sys
import threading
sys.path.append("../")
from conn.sock_parser import sock_parser

# client-side
class async_query_message(threading.Thread):

    def __init__(self, adress, port):
        threading.Thread.__init__(self)
        self.adress = adress
        self.port = port
        self.parser = sock_parser(adress, port)

    def run(self) -> None:
        self.parser.connect_sock_query_message(self.adress, self.port)

        while True:
            query = self.parser.receive_sock_query_message().decode()
            print(query)