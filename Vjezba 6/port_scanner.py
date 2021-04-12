import socket, time
from datetime import datetime

print("Vrijeme pokretanja ovog programa:")
vrijeme = datetime.now()
print(vrijeme)
print('-'*50)

print("Molim vas unesite adresu hosta kojeg želite testirati:")
x = input()
host = socket.gethostbyname(x)
print("Skeniram hosta",x)

print("Unesite od kojeg do kojeg porta želite napraviti skeniranje")
ppocetni = int(input())
pzavrsni = int(input())
print ("Pocetni port>>",ppocetni)
print("Zavrsni port>>",pzavrsni)
start = time.time()
for port in range(ppocetni,pzavrsni):
    print("Skeniram port:", port)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.55)
    rezultat = s.connect_ex((host,port))
    if rezultat == 0:
        print("Port {} je otvoren".format(port))
    else:
        pass
print("Skeniranje portova završeno!!")
runtime = float("%0.2f" % (time.time() - start))
print("Proteklo vrijeme: ", runtime, "sekunda")
    