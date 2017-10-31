import selectors
import socket

sel = selectors.DefaultSelector()


def accept(sk, mk):
    conn, addr = sk.accept()  # Should be ready
    print('accepted', conn, 'from', addr,mask)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read) #新连接注册read回调函数



def read(cn, mk):
    try:
        data = cn.recv(1024)  # Should be ready
    except ConnectionResetError as re:
        print('closing', cn)
        sel.unregister(cn)
        cn.close()
        return
    if data:
        print('echoing', repr(data), 'to', cn)
        cn.send(data)  # Hope it won't block
    else:
        print('closing', cn)
        sel.unregister(cn)
        cn.close()


sock = socket.socket()
sock.bind(('0.0.0.0', 9999))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select() #默认阻塞，有活动连接就返回活动的连接列表
    for key, mask in events:
        callback = key.data #accept
        callback(key.fileobj, mask) #key.fileobj=  文件句柄