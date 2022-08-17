import socket

class ConnSocket():

    def __init__(self, adress, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.adress = adress
        self.port = port

    def __connect__(self) -> None :
        self.sock.connect((self.adress, self.port))

    def __bind__(self) -> None :
        self.sock.bind((self.adress, self.port))

    def __listen__(self) -> None :
        self.sock.listen()

    def __accept__(self) -> tuple :
        return self.sock.accept()

    def __sendall__(self, data) -> None :
        self.sock.sendall(data)

    def __receive__(self) -> bytes :
        return self.sock.recv(1024)

    def __close__(self) -> None :
        self.sock.close()