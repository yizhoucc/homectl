import socket
import sys
try:
    s=socket.socket()
except socket.error as err:
    print("socket creating error {}".format(err)
    )
port=9999
s.bind(('',port))
print("socket bind to port {}".format(port))
s.listen(5)
while True:
    client,addr=s.accept()
    print("connection recieved from {}".format(addr))
    client.send("conn established. from server".encode('utf-8'))


    