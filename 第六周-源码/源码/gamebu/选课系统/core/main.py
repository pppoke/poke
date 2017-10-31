# Author:Game_bu

from core import school
from core import logger
from core import staffs
from core import grade
from core import student
from core import auth

#service logger
service_logger = logger.logger('service')
#system logger
system_logger = logger.logger('system')
def run():
    pass

# import os
# import sys
# import pickle
#
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(base_dir)
#
# from core import school
# from core import staffs
# from core import grade
# from core import student



# school_bj = school.School('老男孩培训北京分校', '北京')
# school_bj.create_course('Python', 10000, 1)
# yuefei = staffs.Teacher('跃飞', 25, 'M', 23000, 'python')
# one_grade = grade.Grade('一班', school_bj.course[0], yuefei)
# school_bj.hire_staffs(yuefei)
# school_bj.create_grade(one_grade)
# jianbo = student.Stu('建波', 23, 'M', school_bj.name, one_grade.name)
# one_grade.stu.add(jianbo)
# one_grade.stu.add(jianbo)
# jianbo.tell()
# one_grade.tell()
# #print(school_bj)

#school_bj.tell()

# with open('school_bj.txt', 'rb') as f:
#     school_bj = pickle.load(f)
#
# school_bj.tell()
# for j in school_bj.course:
#     j.tell()
# for i in school_bj.grade:
#     school_bj.grade[i].tell()
#     print("学生名单：", end='')
#     for q in school_bj.grade[i].stu:
#         print("%s " % q.name, end='')
#     else:
#         print('\n')