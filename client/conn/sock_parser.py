import sys
sys.path.append("../")
import socket

# client-side
class sock_parser():

    def __init__(self, adress, port):
        self.sock_main_stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_message_sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_query_message = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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



    def connect_sock_message_sender(self, adress, port) -> None :
        self.sock_message_sender.connect((adress, port))

    def bind_sock_message_sender(self, adress, port) -> None :
        self.sock_message_sender.bind((adress, port))

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



    def connect_sock_query_message(self, adress, port) -> None :
        self.sock_query_message.connect((adress, port))

    def bind_sock_query_message(self, adress, port) -> None :
        self.sock_query_message.bind((adress, port))

    def listen_sock_query_message(self) -> None :
        self.sock_query_message.listen()

    def accept_sock_query_message(self) -> tuple :
        return self.sock_query_message.accept()

    def sendall_sock_query_message(self, data) -> None:
        self.sock_query_message.sendall(data)

    def receive_sock_query_message(self)-> bytes :
        return self.sock_query_message.recv(1024)

    def close_sock_query_message(self) -> None :
        self.sock_query_message.close()