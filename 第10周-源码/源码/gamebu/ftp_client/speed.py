# Author:Game_bu

import sys


def speed(send_size, filesize):
    count = int(send_size * 100 / filesize)

    for i in range(count):
        print('*', end='')
        sys.stdout.flush()