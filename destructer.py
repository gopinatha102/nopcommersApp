import time


class Test:
    def __init__(self):
        print("Initiations is stated..............")

    def __del__(self):
        print("destructor is activated........")


t1 = Test()
t1 = None
del t1
time.sleep(5)
print("End of application....")