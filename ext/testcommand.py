import socket
import time
import sys
import os
addr0 = ('',43210)
addr1 = ('192.168.48.1',54321)
s0=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s0.bind(addr0)
while True:
    data,addr=s0.recvfrom(1024)
    data.decode()
    print(data)

s0.close()
