# Author:Game_bu


class Stu(object):
    def __init__(self, name, age, sex, school, grade):
        self.name = name
        self.age = age
        self.sex = sex
        self.grade = grade
        self.school = school

    def tell(self):
        print('''
        ---- 学生信息 ----
        姓名:%s
        年龄:%s
        性别:%s
        学校:%s
        班级:%s
        ''' % (self.name, self.age, self.sex, self.school, self.grade))