import socket 
client_socket = socket.socket() 
host = socket.gethostbyname("www.google.com") 
port = 80
 
client_socket.connect((host,port))
print("IP for host name www.google.com is: ", host)
print("The socket has sucessfully connected to Google on port == ",port,", and the IP adress == ", host) 
 
client_socket.close()