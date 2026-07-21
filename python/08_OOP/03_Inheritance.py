'''
Write a Python program to:

- Create a class named Animal.
- Create a method named sound() that displays:
  "Animals make sounds."
- Create another class named Dog that inherits from Animal.
- Create an object of Dog.
- Call the sound() method using the Dog object.
'''
class Animal:
    def sound(self):
        print("Animals make sounds.")
  
class Dog(Animal):
    pass

dog1 = Dog()
dog1.sound()