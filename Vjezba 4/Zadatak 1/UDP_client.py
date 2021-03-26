import socket 

UDPClient_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 
server_adresa = ("127.0.0.2", 9999)

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)

UDPClient_socket.sendto(bytesToSend,server_adresa)
print(UDPClient_socket.recv(1024)) 
UDPClient_socket.close()