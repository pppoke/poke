# Author:Game_bu

import socket

class Client(object):
    def __init__(self):
        self.client = socket.socket()
        self.work_path = ''

    def conn_server(self, addr):
        pass

    def get_file(self, filename):
        pass

    def put_file(self, filename):
        pass

    def ls_home(self):
        pass

    def cd_dir(self):
        pass