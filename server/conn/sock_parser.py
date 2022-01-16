import socket
import json

# server-side
class sock_parser():

    def __init__(self):
        self.sock_main_stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_query_message = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_message_receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data = json.load(open("server_settings.json"))

    def connect_sock_main_stream(self) -> None :
        self.sock_main_stream.connect((self.data["server-ip"], self.data["sockets"]["socket-server-port"]))

    def bind_sock_main_stream(self) -> None :
        self.sock_main_stream.bind((self.data["server-ip"], self.data["sockets"]["socket-server-port"]))

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



    def connect_sock_query_message(self, port) -> None :
        self.sock_query_message.connect((self.data["server-ip"], port))

    def bind_sock_query_message(self, port) -> None :
        self.sock_query_message.bind((self.data["server-ip"], port))

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



    def connect_sock_message_receiver(self, port) -> None :
        self.sock_message_receiver.connect((self.data["server-ip"], port))

    def bind_sock_message_receiver(self, port) -> None :
        self.sock_message_receiver.bind((self.data["server-ip"], port))

    def listen_sock_message_receiver(self) -> None :
        self.sock_message_receiver.listen()

    def accept_sock_message_receiver(self) -> tuple :
        return self.sock_message_receiver.accept()

    def sendall_sock_message_receiver(self, data) -> None:
        self.sock_message_receiver.sendall(data)

    def receive_sock_message_receiver(self)-> bytes :
        return self.sock_message_receiver.recv(1024)

    def close_sock_message_receiver(self) -> None :
        self.sock_message_receiver.close()