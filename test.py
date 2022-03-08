import sys

import sys
class Customer:
    '''Customer class with bank operations'''
    BankName="Durgabank"

    def __init__(self,name,account,balance=0.0):
        self.name=name
        self.account=account
        self.balance=balance
    def Deposit(self,amt):
        self.balance=self.balance+amt
        print("Dopisit Amount is :",self.balance)
    def Withdraw(self,amt):
        if amt >self.balance:
            print("Insufficient Funds...Cannot be Perform this operations")
            sys.exit()
        self.balance=self.balance-amt
        print("After Withdraw amount",self.balance)



print("Welcome To ",Customer.BankName)
name=input("Enter the account Holder name:")
account=int(input("Enter The Account Number :"))
c=Customer(name,account)

while True:
    print("**********************Welcome to DurgaBank***********************")
    print("Choice\n d-Deposit,\n w-Withdraw,\n e-Exit")
    option=input("Enter the option\n")
    if option=="d"or option=="D":
        amt=float(input("Enter the Deposit amount"))
        c.Deposit(amt)
    elif option=="w" or option=="W":
        amt=float(input("Enter the withDraw amount:"))
        c.Withdraw(amt)
    elif option=="e"or option=="E":
        print("Thanks for visiting Durga bank")
        sys.exit()
    else:
        print("Invalid options")

