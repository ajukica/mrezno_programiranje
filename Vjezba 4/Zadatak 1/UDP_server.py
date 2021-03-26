import socket 
UDPServer_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 
host = "127.0.0.2" 
port = 9999 
UDPServer_socket.bind((host,port)) 
print("Waiting for connection...") 
while True:
 bytesAddressPair = UDPServer_socket.recvfrom(1024)
 poruka = bytesAddressPair[0]
 ip = bytesAddressPair[1]
 print('Got Connection from',ip)
