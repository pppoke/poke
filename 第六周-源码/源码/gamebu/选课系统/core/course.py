# Author:Game_bu


class Course(object):
    def __init__(self, name, price, cycle):
        self.name = name
        self.price = price
        self.cycle = cycle

    def tell(self):
        print('''
        ---- 课程信息 ----
        课名:%s
        学费:%s
        周期:%d
        ''' % (self.name, self.price, self.cycle))
