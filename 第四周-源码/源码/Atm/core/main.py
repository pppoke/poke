__author__ = "Alex Li"
import sys

from core import atm_api


def atm():
    navi = ["查询", "转账", "提现", "还款", "管理员登录", "注销登录"]
    while True:
        print("Welcome to gamebu atm")
        for i in range(len(navi)):
            print("{_id}. {_navi}".format(_id=i+1, _navi=navi[i]))
        navi_choice = input("请选择>>>:")
        if navi_choice.isdigit():
            navi_choice = int(navi_choice)
        if navi_choice in range(1, len(navi)+1):
            if navi_choice == 1:
                atm_api.query()
            elif navi_choice == 2:
                atm_api.transfer()
            elif navi_choice == 3:
                pass #cash()
            elif navi_choice == 4:
                atm_api.repayment()
            elif navi_choice == 5:
                atm_api.admin()
            elif navi_choice == 6:
                atm_api.user_logout()
            else:
                pass
        else:
            print("非法输入!")
