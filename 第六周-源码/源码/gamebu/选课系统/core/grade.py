# Author:Game_bu


class Grade(object):
    def __init__(self, name, course_obj, staffs_obj):
        self.name = name
        self.course = course_obj
        self.staffs = staffs_obj
        self.stu = set({})

    def tell(self):
        print('''
        ---- 班级信息 ----
        班名:%s
        导师:%s
        方向:%s第%d期
        学费:%s
        学生数量:%d
        ''' % (self.name, self.staffs.name, self.course.name, self.course.cycle, self.course.price, len(self.stu)))

