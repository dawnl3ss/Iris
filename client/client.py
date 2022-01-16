from threaded.sync_message_sender import sync_message_sender
from threaded.async_query_message import async_query_message
from conn.sock_parser import sock_parser
import time
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
        session_data = None

        while tcp_handshake != True:
            data = parser.receive_sock_main_stream().decode()
            session_data = {"port-message-sender": data.split(":")[0], "port-query-message": data.split(":")[1]}
            print(str(session_data))
            parser.sendall_sock_main_stream("exit".encode())
            parser.close_sock_main_stream()
            tcp_handshake = True
        time.sleep(1)
        async_query_message(adress, int(session_data["port-query-message"])).start()
        sync_message_sender(adress, int(session_data["port-message-sender"])).run()

if __name__ == "__main__":
    main()
