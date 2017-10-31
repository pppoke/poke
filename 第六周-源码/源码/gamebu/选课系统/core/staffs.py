# Author:Game_bu


class Teacher(object):
    def __init__(self, name, age, sex, salary, course):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ---- info of Teacher:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s is teaching course.py [%s]" % (self.name, self.course))
