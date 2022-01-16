from conn.sock_parser import sock_parser
from utils.port_generator import gen_unique_port
from threaded.async_message_receiver import async_message_receiver

def main():
    parser = sock_parser()

    parser.bind_sock_main_stream()
    parser.listen_sock_main_stream()

    while True:
        (client, (client_adress, client_port)) = parser.accept_sock_main_stream()
        print("[+] New client connection : {} | {}".format(client_adress, client_port))

        while True:
            # Envoie du 3way handshake avec les ports de connexions
            port_message_sender = gen_unique_port()
            port_query_message = gen_unique_port()
            client.sendall("{}:{}".format(port_message_sender, port_query_message).encode())

            # Attente de réponse
            if client.recv(1024).decode() == "exit":
                message_receiver = async_message_receiver(port_message_sender).start()
                break
        client.close()

if __name__ == "__main__":
    main()