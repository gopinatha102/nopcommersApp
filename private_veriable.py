# Declaration  of private variables and class
"""
class Test:
    __a = 10
    def __init__(self):
        self.__x=20

    def m1(self):
        print(self.__x)

    @classmethod
    def m2(cls):
        print(cls.__a)

t = Test()
t.m1()
t.m2()
print(t._Test__x)
"""

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def __str__(self):
        return "Student Name is {} and Student RollNo {}".format(self.name,self.rollno)

s1=Student("Durga", 4520)
s2=Student("ravi ", 500)
print(s1)
print(s2)

