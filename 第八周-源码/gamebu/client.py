# Author:Game_bu
import socket

client = socket.socket()

client.connect(('localhost', 9999))

while True:
    ack = input("请输入命令>>")
    if len(ack) == 0: continue
    client.send(ack.encode())
    total_size = client.recv(1024)
    print("结果长度为：", total_size.decode())
    client.send("请返回吧，傻叉!".encode())
    rec_size = 0
    rec = b''
    while True:
        data = client.recv(1024)
        rec_size += len(data)
        rec += data
        if rec_size == int(total_size.decode()):
            break

    print("接收到的长度为：", rec_size)
    print(rec.decode())