__author__ = "Alex Li"

import paramiko
# import Django

transport = paramiko.Transport(('221.122.73.184', 22))
transport.connect(username='monitor', password='9zdataMon!2017')
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
#sftp.put('笔记', '/tmp/test_from_win')
# 将remove_path 下载到本地 local_path
sftp.get('/home/monitor/data', 'fromlinux.txt')

transport.close()