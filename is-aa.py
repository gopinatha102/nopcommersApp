"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatndrink(self):
        print("Eat and drinking..........")


class SE(Person):
    def __init__(self, name, age, eno, empsal):
        super().__init__(name, age)
        self.eno = eno
        self.empsal = empsal

    def work(self):
        print("python coding.......")


s = SE("gopi", 29, 4900, 50000)
print(s.name, s.age, s.eno, s.empsal)
s.eatndrink()
s.work()
"""


class A:

    def m1(self):
        self.x = 10


class B(A):
    def m1(self):
        super().m1()
        self.x = 20

    def disp(self):
        print(self.x)


b = B()
b.m1()
b.disp()
