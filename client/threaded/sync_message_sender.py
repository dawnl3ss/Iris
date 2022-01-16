import sys
sys.path.append("../")
from conn.sock_parser import sock_parser

# client-side
class sync_message_sender():

    def __init__(self, adress, port):
        self.adress = adress
        self.port = port
        self.parser = sock_parser("127.0.0.1", 11111)

    def run(self) -> None:
        self.parser.connect_sock_message_sender(self.adress, self.port)

        while True:
            message = str(input("-> "))
            self.parser.sendall_sock_message_sender(message.encode())