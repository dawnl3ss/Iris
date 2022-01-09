import sys
sys.path.append("../")
from session.session import session
import socket

class sock_parser():

    def __init__(self, adress, port):
        self.sock_main_stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_message_sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_message_receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data = session.session_data
        self.adress = adress
        self.port = port

    def connect_sock_main_stream(self) -> None :
        self.sock_main_stream.connect((self.adress, self.port))

    def bind_sock_main_stream(self) -> None :
        self.sock_main_stream.bind((self.adress, self.port))

    def listen_sock_main_stream(self) -> None :
        self.sock_main_stream.listen()

    def accept_sock_main_stream(self) -> tuple :
        return self.sock_main_stream.accept()

    def sendall_sock_main_stream(self, data) -> None :
        self.sock_main_stream.sendall(data)

    def receive_sock_main_stream(self) -> bytes :
        return self.sock_main_stream.recv(1024)

    def close_sock_main_stream(self) -> None :
        self.sock_main_stream.close()



    def connect_sock_message_sender(self) -> None :
        self.sock_message_sender.connect((self.adress, self.data["port-message-sender"]))

    def bind_sock_message_sender(self) -> None :
        self.sock_message_sender.bind((self.adress, self.data["port-message-sender"]))

    def listen_sock_message_sender(self) -> None :
        self.sock_message_sender.listen()

    def accept_sock_message_sender(self) -> tuple :
        return self.sock_message_sender.accept()

    def sendall_sock_message_sender(self, data) -> None:
        self.sock_message_sender.sendall(data)

    def receive_sock_message_sender(self)-> bytes :
        return self.sock_message_sender.recv(1024)

    def close_sock_message_sender(self) -> None :
        self.sock_message_sender.close()