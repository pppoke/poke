__author__ = "Alex Li"

import socket

HOST = '192.168.1.107'  # The remote host
PORT = 9999  # The same port as used by the server
s = socket.socket()
s.connect((HOST, PORT))
t = True
while t:
    msg = bytes(input(">>:"), encoding="utf8")
    s.sendall(msg)
    data = s.recv(1024)

    #
    print('Received', data.decode())
    #t = False
s.close()
