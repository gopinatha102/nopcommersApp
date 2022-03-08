"""
class Duck:
    def talk(self):
        print("Quack Quack Quack")


class Dog:
    def talk(self):
        print("Bow Bow Bow")


class Cat:
    def talk(self):
        print("Moew Moew Moew")


class Goat:
    def bark(self):
        print("Myaah Myaah Myaah")


l = [Duck(), Dog(), Cat(), Goat()]

for obj in l:
    if hasattr(obj, "talk"):
        obj.talk()
    elif hasattr(obj, "bark"):
        print("Goat class fuction :")
        obj.bark()
"""
# Types of overloading concept
#   1.operator overloading
#   2.methode overloading
#   3.constructor overloading

# operator overloading

#print("*" * 10, "Operator overloading ", "*" * 10)
"""
class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return self.pages+other.pages
    def __eq__(self, other):
        return self.pages==other.pages
b1=Book(100)
b2=Book(200)
print("the Total number of pages is :", b1+b2)
print("The Equal operator ",b1==b2)
"""

"""
# Example 2 overloading operator for + 

class Student:
    def __init__(self, name, markes):
        self.name = name
        self.markes = markes

    def __gt__(self, other):
        return self.markes > other.markes


s1 = Student("durga", 50)
s2 = Student("gopi", 20)
print("Student s1 >s2", s1 > s2)
"""

"""
# Example 2 overloading operator for *

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days


class Timesheet:

    def __init__(self, name, days):
        self.name = name
        self.days = days

    def __mul__(self, other):
        return self.days * other.salary

e = Employee("durga", 1000)
t = Timesheet("durga", 10)
print("Total amount of salary is", e * t)
print("Total Amount of Salary is ", t * e)
"""

# 2. Method Overloading

#print("*" * 10, "Methode Overloading", "*" * 10)

"""
class Test:
    def m1(self):
        print("No -arguments")

    def m1(self,a):
        print("one -arguments")

    def m1(self,a,b):
        print("Two - arguments")

t = Test()
t.m1(10,20)
"""

"""
class Test:
    def sum(self, a=None, b=None, c=None):
        
        if a != None and b != None and c != None:
            print("sum", a + b + c)
            
        elif a != None and b != None:
            print("sum", a + b)
        else:
            print("No arguments")


t = Test()
t.sum(10, 20, 30)
t.sum(10, 20)
t.sum()
"""
"""
# Example 2

class Test:

    def sum(self,*n):
        total=0
        for i in n:
            total=total+i
        print("sum = ",total)

t=Test()
t.sum(10,20)
"""

# 3.constructor overloading
print("*" * 10, "Constructor  Overloading", "*" * 10)

class Test:

    def __init__(self):
        print("No-arguments")

    def __init__(self,a):
        print("One- arguments")

    def __init__(self,a,b):
        print("Two-argument ")

t=Test(10,20)