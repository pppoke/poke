# Author:Game_bu
# import os, sys
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
# sys.path.append(base_dir)
from core import course
from core import staffs


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.grade = {}
        self.staffs = []
        self.course = []

    def create_course(self, name, price, cycle):
        new_course = course.Course(name, price, cycle)
        self.course.append(new_course)
        return new_course

    def hire_staffs(self, staffs_obj):
        self.staffs.append(staffs_obj)

    def create_grade(self, grade_obj):
        if grade_obj.name in self.grade:
            print("该班级名称[%s]已存在，请先删除。" % grade_obj.name )
            return None
        if grade_obj.course not in self.course:
            print("贵校没有[%s]第%d期课程，请先创建。" % (grade_obj.course.name, grade_obj.course.cycle))
            return None
        if grade_obj.staffs not in self.staffs:
            print("贵校没有[%s]这名教师，请先聘用。" % grade_obj.staffs.name)
            return None
        else:
            self.grade[grade_obj.name] = grade_obj

    def tell(self):
        print('''
        ---- 学校信息 ----
        校名:%s
        地址:%s
        班级数量:%d
        老师数量:%d
        课程数量:%d
        ''' % (self.name, self.addr, len(self.grade), len(self.staffs), len(self.course)))


