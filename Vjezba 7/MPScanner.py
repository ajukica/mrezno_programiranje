import socket
from datetime import datetime
import multiprocessing
from multiprocessing import Pool
from Local_Machine_Info import print_machine_info


socket.setdefaulttimeout(0.55)

print_machine_info()

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
            print('Port je otvoren!', port)
        con.close()
    except:
        pass

if __name__ == '__main__':
    

    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    ports = range(ppocetni, pzavrsni)
    lista = [(host, port) for port in ports]

    pool = Pool(multiprocessing.cpu_count() * 2)

    for port, status in pool.imap(portscan, lista):
        if status:
            print('Port', port, 'je otvoren!')

print("Skeniranje portova zavrseno!")
runtime = float("%0.2f" % (time.time() - start))
print("Proteklo vrijeme: ", runtime, "sekunda")
    
