from conn.conn_socket import ConnSocket

def main():
    sock = ConnSocket("127.0.0.1", 23456)
    sock.__bind__()
    sock.__listen__()

    while True:
        (client, (client_adress, client_port)) = sock.__accept__()
        print("[+] New client connection : {} | {}".format(client_adress, client_port))
        client.close()

if __name__ == "__main__":
    main()