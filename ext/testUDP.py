import socket
import time
import sys
import os
addr0 = ('',43210)
addr1 = ('192.168.48.1',54321)
s0=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
i=1
while True:
    message="hello world"
    s1.sendto(message.encode('utf8'), addr1)
    #i=i+1
    time.sleep(1)
    #if(i>=10):
    #   break
s0.close()
s1.close()