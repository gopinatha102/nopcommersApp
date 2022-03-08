class G:
    def m1(self):
        print("Granada father ")


class F(G):
    def m2(self):
        print("Father .....")
        print("accessing you and Granada father methods")


class U(F):
    def m3(self):
        print("your only")
        print("Accessing you and father and Granada father methods")


u = F()
#u.m3()
u.m2()
u.m1()

