__Author__ = "Gamebu"

import select
import socket
import queue

server = socket.socket()
server.bind(('0.0.0.0', 9998))
server.listen(20)
inputs = []
outputs = []
mydic = {}
server.setblocking(False)

inputs.append(server)
while True:
    readable, writeable, exceptable = select.select(inputs, outputs, inputs)
    for r in readable:
        if r is server:
            conn, addr = r.accept()
            inputs.append(conn)
            print("新连接：", conn)
            mydic[conn] = queue.Queue()
        else:
            try:
                rec = r.recv(1024)
                if not rec:
                    raise ConnectionResetError('客户端正常关闭！')
                print("receive:", rec)
                mydic[r].put(rec.decode().upper())
                if r not in outputs:
                    outputs.append(r)
            except ConnectionResetError as conn_error:
                print(conn_error)
                exceptable.append(r)
    for w in writeable:
        send_str = mydic[w].get().encode()
        w.send(send_str)
        outputs.remove(w)
    for e in exceptable:
        try:
            inputs.remove(e)
            outputs.remove(e)
            mydic.pop(e)
        except (ValueError, KeyError) as ex:
            pass
        # finally:
        #     print("异常清理已完成!")

