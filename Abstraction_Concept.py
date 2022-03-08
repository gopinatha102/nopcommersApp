# Abstraction Concept
#  1.Abstraction Method
#  2.Abstraction Class
#  3.Interface


# Abstraction Methode

from abc import *

""""
# Declaration of Abstract Methode 

class Vehicle():

    @abstractmethod
    def getnoofwhelles(self):
        pass


# Declaration of Abstraction class

class Fruit(ABC):

    @abstractmethod
    def taste(self):
        pass
"""

# Implementation by using Chilled class creating object
"""
class Vehicle(ABC):

    @abstractmethod
    def getnoofwhells(self):
        pass

class Bus(Vehicle):

    def getnoofwhells(self):
        return 8

class Auto(Vehicle):

    def getnoofwhells(self):
        return 3
b=Bus()
print(b.getnoofwhells())

a=Auto()
print(a.getnoofwhells())
"""


# How to implements interface v/s abstract v/s concretecls
"""
class Vechile(ABC):

    @abstractmethod
    def m1(self):
        pass

    def m2(self):
        pass

    def m3(self):
        pass


class ImplCls(Vechile):

    def m1(self):
        print("m1 implemented")

    def m2(self):
        print("m2 implemented")


class ConctrCls(ImplCls):

    def m3(self):
        print("m3 implemented")

c=ConctrCls()
c.m1()
c.m2()
c.m3()
"""

# Example 2
