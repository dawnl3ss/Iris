import sys
import threading
sys.path.append("../")
from conn.sock_parser import sock_parser
from session.session import session

# server-side
class async_message_receiver(threading.Thread):

    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.parser = sock_parser()

    def run(self) -> None:
        self.parser.bind_sock_message_receiver(self.port)
        self.parser.listen_sock_message_receiver()
        (client, (client_adress, client_port)) = self.parser.accept_sock_message_receiver()

        while True:
            message = client.recv(1024).decode()
            session.session_messages.append(message)
            #print(session.session_messages)