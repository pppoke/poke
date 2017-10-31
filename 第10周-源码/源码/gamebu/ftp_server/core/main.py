import selectors
import socket
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

sel = selectors.DefaultSelector()

ser_dic = {}

def accept(sk, mk):
    conn, addr = sk.accept()  # Should be ready
    print('accepted', conn, 'from', addr, mask)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, handle)  # 新连接注册read回调函数

def put(*args):
    def put_send(*args):
        cn = args[0]
        mk = args[1]
        print('24 test log')
        cn.send(json.dumps(response).encode('utf-8'))
    def put_recv(*args):
        cn = args[0]
        mk = args[1]
        global received_size
        if received_size == filesize:
            ser_dic[cn]['limit'] -= received_size
            with open('%s/conf/%s' % (BASE_DIR, ser_dic[cn]['username']), 'w') as p:
                json.dump(ser_dic[cn], p, indent=4)
            f.close()
            os.renames(filename + ".temp", filename)
            print("file [%s] has uploaded..." % os.path.basename(filename))
            return
        data = cn.recv(1024*8)
        # self.request.send(b'come.on')
        if data == b'interrupt':
            print('user interrupt')
            f.close()
        f.write(data)
        received_size += len(data)
    global ser_dic
    cmd_dic = args[0]
    cn = args[1]
    mk = args[2]
    filename = ser_dic[cn]['workpath'] + '/' + os.path.basename(cmd_dic["filename"])
    filesize = cmd_dic["size"]
    response = [0, 0]
    if filesize > ser_dic[cn]['limit']:
        response = [1, 0]
        sel.unregister(cn)
        sel.register(cn, selectors.EVENT_WRITE, put_send)
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
    sel.unregister(cn)
    sel.register(cn, selectors.EVENT_WRITE, put_send)
    received_size = response[1]
    # while True:
    #     if received_size == filesize:
    #         ser_dic[cn]['limit'] -= received_size
    #         with open('%s/conf/%s' % (BASE_DIR, ser_dic[cn]['username']), 'w') as p:
    #             json.dump(ser_dic[cn], p, indent=4)
    #         f.close()
    #         os.renames(filename + ".temp", filename)
    #         print("file [%s] has uploaded..." % os.path.basename(filename))
    #         return
    sel.unregister(cn)
    sel.register(cn, selectors.EVENT_READ, put_recv)



def handle(cn, mk):
    try:
        data = cn.recv(1024).strip()
        print("{} wrote:".format(cn.getpeername()), data)
        cmd_dic = json.loads(data.decode())
        action = cmd_dic["action"]
        if action in func_str:
            func = func_str[action]
            func(cmd_dic, cn, mk)
        print('用户信息', ser_dic)

    except ConnectionResetError as e:
        print("err", e)

def auth(*args):
    global ser_dic
    cli_msg = args[0]
    cn = args[1]
    mk = args[2]
    username = cli_msg['username']
    password_md5 = cli_msg['password']
    if cli_msg['register']:
        cli_msg['workpath'] = '%s/data/%s' % (BASE_DIR, username)
        os.makedirs(cli_msg['workpath'])
        cli_msg['limit'] = 104857600
        cli_msg.pop('action')
        cli_msg.pop('register')
        with open('%s/conf/%s' % (BASE_DIR, username), 'w') as f:
            json.dump(cli_msg, f, indent=4)
        with open('%s/conf/%s' % (BASE_DIR, username), 'r') as f:
            ser_dic[cn] = json.load(f)
        sel.unregister(cn)
        sel.register(cn, selectors.EVENT_WRITE, auth1)
    else:
        with open('%s/conf/%s' % (BASE_DIR, username), 'r') as f:
            ser_dic[cn] = json.load(f)
        if ser_dic[cn]['password'] == password_md5:
            sel.unregister(cn)
            sel.register(cn, selectors.EVENT_WRITE, auth1)
        else:
            ser_dic.remove(cn)
            sel.unregister(cn)
            sel.register(cn, selectors.EVENT_WRITE, auth0)

def auth1(cn, mk=0):
    cn.send(b'1')
    sel.unregister(cn)
    sel.register(cn, selectors.EVENT_READ, handle)

def auth0(cn, mk=0):
    cn.send(b'0')
    sel.unregister(cn)
    sel.register(cn, selectors.EVENT_READ, handle)


if __name__ == "__main__":
    func_str = {'accept': accept,
                'auth': auth,
                'put': put}
    sock = socket.socket()
    sock.bind(('0.0.0.0', 9999))
    sock.listen(100)
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)

    while True:
        events = sel.select()  # 默认阻塞，有活动连接就返回活动的连接列表
        for key, mask in events:
            callback = key.data  # accept
            callback(key.fileobj, mask)  # key.fileobj=  文件句柄