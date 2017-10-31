__Author__ = "Gamebu"

from multiprocessing import Process, Manager
import os

def f(di, li):
    di[os.getpid()] = os.getpid()
    li.append(os.getpid())
    print(di)
    print(li)

if __name__ == '__main__':
    with Manager() as ma:
        d = ma.dict()
        l = ma.list(range(3))

        pro_obj = []

        for i in range(10):
            p = Process(target=f, args=(d, l))
            pro_obj.append(p)
            p.start()
        for proc in pro_obj:
            proc.join()
        print("master dict:", d)
        print("master list:", l)
