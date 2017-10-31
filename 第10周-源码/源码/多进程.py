import multiprocessing
import time
import threading
__Author__ = "Gamebu"


def thread():
    print("thread:%s" % threading.get_ident())

def run(name):
    print("hello {name}".format(name=name))
    t = threading.Thread(target=thread,)
    t.start()
    time.sleep(2)

print("name", __name__)
if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run, args=('gamebu %s' %i, ))
        p.start()