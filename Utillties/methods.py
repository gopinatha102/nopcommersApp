"""class Student:

    def __init__(self, student_name, student_rollno, student_marks):
        self.name = student_name
        self.rollno = student_rollno
        self.marks = student_marks

    def display(self):
        print("Student name Is :", self.name)
        print("Student Rollno is :", self.rollno)
        print("Student Marks is:", self.marks)

    def grads(self):
        if self.marks >= 60:
            print("First Class Marks:", self.marks)
        elif self.marks >= 50:
            print("Second Class :", self.marks)
        elif self.marks >= 35:
            print("Just Pass:", self.marks)
        else:
            print("Your Are Failed ")


n = int(input("Enter The Number of Students:"))
for i in range(n):
    name = input("Enter The Student Name:")
    rollno = int(input("Enter The Student Rollno:"))
    marks = int(input("Enter The Student Marks:"))
    s = Student(name, rollno, marks)
    s.display()
    s.grads()
    print()
"""


# using setter and getter Functions
class Student:
    def __init__(self):
        self.marks = marks
        self.name = name

    def setName(self, name):
        pass

    def getName(self):
        return self.name

    def setMarks(self, marks):
        pass

    def getMarks(self):
        return self.marks


n = int(input("Enter the Number of Students:"))
for i in range(n):
    s = Student()
    name = input("Enter The Name of Student:")
    s.setName(name)
    marks = int(input("Enter The marks of student:"))
    s.setMarks(marks)

    print("Hi this is:", s.getName())
    print("Marks of Student is :", s.getMarks())
