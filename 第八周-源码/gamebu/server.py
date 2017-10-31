# Author:Game_bu

import socket, os, sys

server = socket.socket()
server.bind(('localhost', 9999))

server.listen()

while True:
    conn, addr = server.accept()
    print("新客户端：", addr)
    sys.stdout.flush()
    while True:
        print("等待客户端输入...")
        sys.stdout.flush()
        ack = conn.recv(1024)
        zz = ack.decode()
        print(zz)
        res = os.popen(zz)
        print(dir(res))
        res = res.read()
        if len(res) ==0:
            res = "cmd has no output..."
        res_byte = res.encode()
        conn.send(str(len(res_byte)).encode())
        res_ack = conn.recv(1024)
        print("客户端要求发送结果...")
        sys.stdout.flush()
        conn.send(res_byte)