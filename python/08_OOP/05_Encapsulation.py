'''
Write a Python program to:

- Create a class named Student.
- Create a constructor that stores the student's name
  in a private variable named __name.
- Create a method named display() that displays the student's name.
- Create an object of the Student class.
- Call the display() method.
'''
class Student:
    def __init__(self):
        self.__name = "Ridhi"

    def display(self):
        print("Student name:", self.__name)

student1 = Student()
student1.display()
