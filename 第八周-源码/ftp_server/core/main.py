
import socketserver
import json
import os
import sys
import threading

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class MyTCPHandler(socketserver.BaseRequestHandler):

    def put(self, *args):
        cmd_dic = args[0]
        filename = self.ser_dic['workpath'] + '/' + os.path.basename(cmd_dic["filename"])
        filesize = cmd_dic["size"]
        response = [0, 0]
        if filesize > self.ser_dic['limit']:
            response = [1, 0]
            self.request.send(json.dumps(response).encode('utf-8'))
            return
        elif os.path.isfile(filename):
            if cmd_dic['overridden']:
                os.remove(filename)
            else:
                filename = filename + '.new'
            f = open(filename+'.temp', "wb")
        elif os.path.isfile(filename+'.temp'):
            temp_size = os.stat(filename + '.temp').st_size
            response = [2, temp_size]
            f = open(filename + '.temp', "ab")
        else:
            f = open(filename + ".temp", "wb")
        self.request.send(json.dumps(response).encode('utf-8'))
        received_size = response[1]
        while True:
            if received_size == filesize:
                self.ser_dic['limit'] -= received_size
                with open('%s/conf/%s' % (BASE_DIR, self.ser_dic['username']), 'w') as p:
                    json.dump(self.ser_dic, p, indent=4)
                f.close()
                os.renames(filename + ".temp", filename)
                print("file [%s] has uploaded..." % os.path.basename(filename))
                return
            data = self.request.recv(1024*8)
            # self.request.send(b'come.on')
            if data == b'interrupt':
                break
            f.write(data)
            received_size += len(data)
            print('received_size ', received_size)
            print('filesize ', filesize)
        print('user interrupt')
        f.close()

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]), self.data)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic["action"]
                if hasattr(self, action):
                    func = getattr(self, action)
                    func(cmd_dic)
                print('用户信息', self.ser_dic)

            except ConnectionResetError as e:
                print("err", e)
                break

    def auth(self, *args):
        username = args[0]['username']
        password_md5 = args[0]['password']
        if args[0]['register']:
            args[0]['workpath'] = '%s/data/%s' % (BASE_DIR, username)
            os.makedirs(args[0]['workpath'])
            args[0]['limit'] = 104857600
            args[0].pop('action')
            args[0].pop('register')
            with open('%s/conf/%s' % (BASE_DIR, username), 'w') as f:
                json.dump(args[0], f, indent=4)
            with open('%s/conf/%s' % (BASE_DIR, username), 'r') as f:
                self.ser_dic = json.load(f)
            self.request.send(b'1')
        else:
            with open('%s/conf/%s' % (BASE_DIR, username), 'r') as f:
                self.ser_dic = json.load(f)
            if self.ser_dic['password'] == password_md5:
                self.request.send(b'1')
            else:
                self.request.send(b'0')


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    semaphore = threading.BoundedSemaphore(5)
    server.serve_forever()