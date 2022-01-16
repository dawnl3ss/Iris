from threaded.sync_message_sender import sync_message_sender
from conn.sock_parser import sock_parser
from session.session import session
import os

def main():
    adress = str(input("#~ Put the server ip-adress : "))
    port = int(input("#~ Put the connection port : "))
    parser = sock_parser(adress, port)
    tcp_handshake = False

    parser.connect_sock_main_stream()
    os.system("cls")
    print("[+] You are currently chatting on server {} with port {}".format(adress, port))

    while True:
        while tcp_handshake != True:
            data = parser.receive_sock_main_stream().decode()
            session.session_data = {"port-message-sender": data.split(":")[0], "port-query_message": data.split(":")[1]}
            print(str(session.session_data))
            parser.sendall_sock_main_stream("exit".encode())
            parser.close_sock_main_stream()
            tcp_handshake = True
        message_sender = sync_message_sender(adress, int(session.session_data["port-message-sender"])).run()
    #demarrer les deux async task send et receive messag

if __name__ == "__main__":
    main()
