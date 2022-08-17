from conn.conn_socket import ConnSocket
import os

def main():
    adress = str(input("#~ Put the server ip-adress : "))
    port = int(input("#~ Put the connection port : "))

    sock = ConnSocket(adress, port)
    sock.__connect__()

    os.system("cls")

    print("[+] You are currently chatting on server {} with port {}".format(adress, port))
    sock.__close__()

if __name__ == "__main__":
    main()
