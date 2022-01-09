from conn.sock_parser import sock_parser
from utils.port_generator import gen_unique_port
import os
import json

def main():
    parser = sock_parser()

    parser.bind_sock_main_stream()
    parser.listen_sock_main_stream()

    while True:
        (client, (client_adress, client_port)) = parser.accept_sock_main_stream()
        print("[+] New client connection : {} | {}".format(client_adress, client_port))

        while True:
            # Envoie du message
            client.sendall("{}:{}".format(gen_unique_port(), gen_unique_port()).encode())

            # Attente de réponse
            if client.recv(1024).decode() == "exit": break
        client.close()

if __name__ == "__main__":
    main()