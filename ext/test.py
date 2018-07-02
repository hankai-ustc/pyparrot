import socket
import time
import sys
import os
addr0 = ('',8888)
addr1 = ('192.168.48.1',9999)
s0=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s0.bind(addr0)
#os.system('netsh -c i i set neighbors "ETH" 192.168.48.1 be-1c-a8-d5-26-cd')
os.system('netsh -c i i set neighbors "ETH" 192.168.48.1 8A-9F-8E-51-3F-2D')
while True:
    message,addr= s0.recvfrom(1024)
    message=message.decode()
    if message=="ap1":
        print("change to ap1")
        os.system('netsh -c i i set neighbors "ETH" 192.168.48.1 be-1c-a8-d5-26-cd')
        #time.sleep(0.1)
        s1.sendto(message.encode('utf8'),addr1)
    if message=="ap2":
        print ("change to ap2")
        os.system('netsh -c i i set neighbors "ETH" 192.168.48.1 8a-9f-8e-51-3f-2d')
        #time.sleep(0.1)
        s1.sendto(message.encode('utf8'),addr1)
    if message=="ap3":
        print ("change to ap3")
        os.system('netsh -c i i set neighbors "ETH" 192.168.48.1 da-3a-fa-2d-bf-f9')
        #time.sleep(0.1)
        s1.sendto(message.encode('utf8'), addr1)
