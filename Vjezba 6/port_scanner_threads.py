import socket, threading, time 
from queue import Queue
from datetime import datetime

socket.setdefaulttimeout(0.55)
print_lock = threading.Lock()

queue = Queue()
open_ports = []
 
print("Vrijeme pokretanja ovog programa:")
now = datetime.now()
print(now)
print('-'*50)

print("Molim vas unesite adresu hosta kojeg želite testirati:")
x = input()
host = socket.gethostbyname(x)
print("Skeniram hosta",x)

print("Unesite od kojeg do kojeg porta želite napraviti skeniranje?")
ppocetni = int(input())
pzavrsni = int(input())
print("Pocetni port>>",ppocetni)
print("Zavrsni port>>",pzavrsni)

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((host, port))
        with print_lock:
            print('Port je otvoren', port)
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()
start = time.time()

for x in range(200):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
  


for worker in range(ppocetni, pzavrsni):
    q.put(worker)
q.join()

print("Skeniranje portova zavrseno!!")
runtime = float("%0.2f" % (time.time() - start))
print("Proteklo vrijeme: ", runtime, "sekunda")
    
