import socket
import ssl
import datetime
from Local_Machine_Info import print_machine_info
print(datetime.datetime.now())
print_machine_info()

from SSL_Server import HOST as SERVER_HOST
from SSL_Server import PORT as SERVER_PORT

HOST,PORT = "127.0.0.5", 4000


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client = ssl.wrap_socket(client, keyfile="kljuc.pem", certfile="cert.pub")

if __name__ == "__main__":
    client.bind((HOST, PORT))
    client.connect((SERVER_HOST, SERVER_PORT))

    while True:
        from time import sleep

        client.send("Konekcija!".encode("utf-8"))
        sleep(1)