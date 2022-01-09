import sys
import threading
sys.path.append("../")
from server.conn.sock_parser import sock_parser

class async_message_receive(threading.Thread):

    def __init__(self, adress, port):
        threading.Thread.__init__(self)
        self.adress = adress
        self.port = port
        self.parser = sock_parser()

    def run(self) -> None:
        self.parser.bind_sock_message_receiver(self.adress, self.port)
        self.parser.listen_sock_message_receiver()
        (client, (client_adress, client_port)) = self.parser.accept_sock_message_receiver()