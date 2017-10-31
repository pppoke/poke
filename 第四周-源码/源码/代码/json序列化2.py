__author__ = "Alex Li"
#import json

import pickle

class Test(object):
    def __init__(self):
        self.name = 0
        self.age = 18

#liu = Test()



def sayhi1(name):
    print("hello,",name)

def sayhi(name):
    print("hello1111,",name)
# info = {
#     'name':'alex',
#     'age':22,
#     'func':sayhi,
#     'stu':liu
# }


f = open("test.text","rb")

#pickle.dump(info,f) #f.write( pickle.dumps( info) )
#print(sayhi)
info = pickle.load(f)
print(info)
print(info['stu'].age)
info['func']('name')
f.close()
