import socket
import datetime
import main

from main import print_machine_info
print_machine_info()

print (datetime.datetime.now())
host = socket.gethostname()
port = 12345

echo_server = socket.socket()
echo_server.bind((host,port))
echo_server.listen(5)

while True:
    print ("Cekam klijente...")
    conn,addr = echo_server.accept()
    print(("Spojen: ", addr))
    data = conn.recv(1024).decode('utf-8')
    if (data == "Ante Jukica"):
        print("Taj unos nije podrzan")
        break
    print (data)
    break
conn.close()