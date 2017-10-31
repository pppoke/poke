#_author__ = "gamebu"

import socket
import json
import os
import hashlib
import sys
import speed
import time


class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()
        self.auth = False

    @staticmethod
    def help():
        msg = '''
        ls
        pwd
        cd <path>
        get <filename>
        put <filename>
        '''
        print(msg)

    def connect(self, ip, port):
        self.client.connect((ip, port))
        while not self.auth:
            self.__authenticate()
        else:
            print("Welcome,%s" % self.username)

    def __authenticate(self):
        self.username = input('login：').strip()
        password_md5 = hashlib.md5()
        password = input('password：').strip()
        password_md5.update(password.encode())
        msg_dic = {
            "action": "auth",
            "username": self.username,
            "password": password_md5.hexdigest(),
            "register": False
        }
        print('send', json.dumps(msg_dic).encode("utf-8"))
        self.client.send(json.dumps(msg_dic).encode("utf-8"))
        server_response = self.client.recv(1024)
        if server_response.decode() == '1':
            self.auth = True
        else:
            print('Login incorrect')

    def interactive(self):
        while True:
            cmd = input(">>").strip()
            if len(cmd) == 0:
                continue
            cmd_str = "cmd_%s" % cmd.split()[0]
            if hasattr(self, cmd_str):
                func = getattr(self, cmd_str)
                func(cmd)
            else:
                self.help()

    def cmd_put(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if not os.path.isfile(filename):
                print(filename, "is not exist")
                return
            filesize = os.stat(filename).st_size
            msg_dic = {
                "action": "put",
                "filename": filename,
                "size": filesize,
                "overridden": True
            }
            self.client.send(json.dumps(msg_dic).encode("utf-8"))
            server_response = json.loads(self.client.recv(1024).decode())
            if server_response[0] == 1:
                print("Lack of space,back...")
                return
            seek_size = 0
            if server_response[0] == 2:
                seek_size = server_response[1]
            f = open(filename, "rb")
            f.seek(seek_size)
            print("<sending %s>" % filename, end='')
            speed.speed(seek_size, filesize)
            try:
                for line in f:
                    send_size = self.client.send(line)
                    # self.client.recv(1024)
                    speed.speed(send_size, filesize)
                else:
                    print("\nfile upload success...")
            except KeyboardInterrupt:
                time.sleep(0.5)
                self.client.send(b'interrupt')
                print("user interrupt")
            finally:
                f.close()

    def cmd_get(self):
        pass


ftp = FtpClient()
ftp.connect("localhost", 9999)
ftp.interactive()
