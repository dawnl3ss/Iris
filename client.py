from conn.conn_socket import ConnSocket
import os

def main():
    global adress, port, exit, username
    sock = ConnSocket(adress, port)
    sock.__connect__()
    os.system("cls")

    print("[+] You are currently chatting on server {} with port {}".format(adress, port))

    while not exit:
        print('test')

    sock.__close__()

if __name__ == "__main__":
    adress = str(input("#~ Put the server ip-adress : "))
    port = int(input("#~ Put the connection port : "))
    username = str(input("#~ Choose your username : "))
    exit = False
    if username.replace(" ", "") != "": main()
    else: print("You can't have this username")
