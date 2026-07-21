'''
Write a Python program to:

- Import ABC and abstractmethod from the abc module.
- Create an abstract class named Animal.
- Create an abstract method named sound().
- Create a child class named Dog.
- Implement the sound() method in the Dog class to display:
  "Dog barks."
- Create an object of Dog.
- Call the sound() method.
'''
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog Barks.")

dog1 = Dog()
dog1.sound()