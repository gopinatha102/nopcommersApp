"""class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print("Student name is :",self.name)
        print("Student marks is :",self.marks)

class Test:
    def modifcation(stu):
        stu.marks=stu.marks+10
        stu.display()


s=Student("gopinatha",50)
Test.modifcation(s)"""

"""
class University:
    university_name = "Reva University"

    def university_name1(self):
        print("University Name is :", University.university_name)

    class Department:
        def __init__(self, name, facultity):
            self.name = name
            self.facultity = facultity

        def display(self):
            print("Department Name is :", self.name)
            print("Number of Facultity is :", self.facultity)


# u=University()
# u.university_name1()
s = University().Department("ECE", 70).display()
#s.display()
"""

"""
class Person:
    def __init__(self):
        self.name = "Gopinatha"
        self.db = self.Dob()

    def display(self):
        print("Name of the Person is :", self.name)

    class Dob:
        def __init__(self):
            self.dd = 28
            self.mm = 10
            self.yyyy = 1992

        def display(self):
            print("Dob {}-{}-{}".format(self.dd, self.mm, self.yyyy))


p = Person()
p.display()
p.db.display()
"""

class Human():
    def __init__(self):
        self.name="Sunny"
        self.head=self.Head()
        self.brian=self.Brain()

    def display(self):
        print("Human name is ",self.name)

    class Head():
        def talk(self):
            print("Talking......")

    class Brain:
        def thing(self):
            print("thing....")
h=Human()
h.display()
h.head.talk()
h.brian.thing()