class P:

    def m1(self):
        print("parent class...........")


class C(P):

    def m2(self):
        print("childed class...... ...")


c = C()
c.m1()
c.m2()
