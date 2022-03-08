"""class A:
    a = 888

    def m1(self):
        self.a = 10


class B(A):
    def __init__(self):
        super().m1()
        print(super().a)
        print(self.a)


b = B()
b.m1()
"""


class P:

    def __init__(self):
        self.x = 10
    def m1(self):
        self.x=555

class C(P):

    def __init__(self):
        self.x = 20
        super().__init__()
        print(self.x)
        super().m1()
        print(self.x)

c = C()
