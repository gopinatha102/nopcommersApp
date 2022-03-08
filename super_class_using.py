class P:
    a = 10

    def __init__(self):
        print("Constructor...........")

    def m1(self):
        print("instante methode....")

    @classmethod
    def m2(cls):
        print("Class method....")

    @staticmethod
    def m3():
        print("Static Methode.......")


class C(P):
    def __int__(self):
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()

    def m4(self):
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()

    @classmethod
    def m5(cls):
        #    super().__init__()
        print(super().a)
        # super().m1()
        super().m2()
        super().m3()

    @staticmethod
    def m6():
        # super().__init__()
        # print(super().a)
        # super().m1()
        super().m2()
        super().m3()


c = C()
print("*" * 10, "chilled instant  methode call  ", "*" * 10)
c.m4()
print("*" * 10, "chilled class methode call  ", "*" * 10)
c.m5()
print("*" * 10, "chilled static  methode call  ", "*" * 10)
c.m6()
