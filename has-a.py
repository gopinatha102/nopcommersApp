class Car:
    def __init__(self, car_name, car_model, car_colour):
        self.name = car_name
        self.model = car_model
        self.colour = car_colour

    def getinfo(self):
        print("Car Name is ", self.name)
        print("Car model is ", self.model)


class Employee:
    def __init__(self, ename, eid, car):
        self.ename = ename
        self.eid = eid
        self.car = car

    def display(self):
        print("Employee Name is", self.ename)
        print("Employee Id is ", self.eid)
        print("Employee car Details")
        self.car.getinfo()

c = Car("BMW", 145, "Black")
e = Employee("gopinath", 4900, c)
e.display()