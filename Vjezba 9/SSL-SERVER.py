import socket,ssl,sys,datetime
from Local_Machine_Info import print_machine_info
print(datetime.datetime.now())
print_machine_info()

HOST,PORT = "127.0.0.5", 40000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server = ssl.wrap_socket(server, server_side=True, keyfile="kljuc.pem", certfile="cert.pum")

if __name__ == "__main__":
    server.bind((HOST, PORT))
    server.listen(0)

    while True:
        connection, client_address = server.accept()
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")