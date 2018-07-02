import socket

address = ('192.168.109.161', 6655)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

while True:
    data, addr = s.recvfrom(2048)
    if not data:
        print("client has exist")
        break
    print (data)
    print ("received %s from %s" %(data,addr))
s.close()