import socket
import datetime
import main
from main import print_machine_info

print_machine_info()
print (datetime.datetime.now())
host = socket.gethostname()
port = 12345

client_socket = socket.socket()

client_socket.connect((host,port))

print ("Unesite tekst")
tekst = input()
client_socket.sendall(tekst.encode('utf-8'))

data = client_socket.recv(1024)

print (data)
client_socket.close()

