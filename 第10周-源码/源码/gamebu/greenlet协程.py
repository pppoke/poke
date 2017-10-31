__Author__ = "Gamebu"

from greenlet import greenlet


def f1():
    print("function \033[32;1mf1\033[0m start")
    g2.switch()
    print("function \033[32;1mf1\033[0m end")
    g2.switch()


def f2():
    print("function \033[31;1mf2\033[0m start")
    g1.switch()
    print("function \033[31;1mf2\033[0m end")


if __name__ == '__main__':
    g1 = greenlet(f1)
    g2 = greenlet(f2)
    g1.switch()