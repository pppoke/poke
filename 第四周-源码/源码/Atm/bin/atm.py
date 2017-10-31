__author__ = "Alex Li"

import os
import sys, pickle, time

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
from conf import settings
from core import main

# ad = {"gamebu" : {"passwd": "gamebu"}, "yuefei": {"passwd": "yuefei"}, "piqiu": {"passwd": "piqiu"}}
# ud = {"xuecheng": {"passwd": "xuecheng", "limit": 20000.0,"balance": 20000.0, "interest": 0.05,"state": "active" } }
# dd = {"admin": ad ,"user": ud }

# with open(BASE_DIR+"/conf/db.bat", 'rb') as fp:
#      print(pickle.load(fp))

main.atm()
#print(settings.xxxxx())

#print(time.strftime('%Y-%m-%d %X'))

# all_user_dict = {'admin': {'gamebu': {'passwd': 'gamebu'}, 'yuefei': {'passwd': 'yuefei'}, 'piqiu': {'passwd': 'piqiu'}}, 'user': {'xuecheng': {'passwd': 'xuecheng', 'limit': 20000.0, 'balance': 20000.0, 'interest': 0.05, 'state': 'active'}, 'dongge': {'passwd': 'dongge', 'limit': 11000.0, 'balance': 11000.0, 'interest': 0.04, 'state': 'active'}}}
#
# print(type(all_user_dict['user']))
# all_user_dict['user'].k
