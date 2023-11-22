from conn.conn_socket import ConnSocket
from handler.server_handler import on_client_connect

def main():
    sock = ConnSocket("127.0.0.1", 12345)
    sock.__bind__()
    sock.__listen__()

    while True:
        (client, (client_adress, client_port)) = sock.__accept__()
        on_client_connect(client, client_adress, client_port)
        client.close()

if __name__ == "__main__":
    main()