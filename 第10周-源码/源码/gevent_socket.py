__author__ = "Alex Li"

import sys
import socket
import time
import gevent

from gevent import socket, monkey

monkey.patch_all()


def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    s.setblocking(False)
    while True:
        try:
            cli, addr = s.accept()
            gevent.spawn(handle_request, cli)
        except Exception as e:
            print("error", e)
            time.sleep(2)
        print('test')


def handle_request(conn):
    try:
        while True:
            try:
                conn.setblocking(False)
                print('conn>test')
                data = conn.recv(1024)
                print("recv:", data)
                conn.send(data.decode().upper().encode())
                if not data:
                    break
            except BlockingIOError as e:
                print('line 41', e)
                time.sleep(2)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()


if __name__ == '__main__':
    server(9999)
