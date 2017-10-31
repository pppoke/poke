#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

_ag = 18

count = 0
while count < 3:
    xx = int(input("ge:"))
    if _ag == xx:
        print("good")
        break
    elif _ag < xx:
        print("think smaller")
    else:
        print("think bigger")
    count += 1
else:
    print("fuck off")
print("done")
