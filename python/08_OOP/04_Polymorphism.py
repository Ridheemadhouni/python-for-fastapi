'''
Write a Python program to:

- Create a class named Dog with a method sound() that displays:
  "Dog barks."
- Create another class named Cat with a method sound() that displays:
  "Cat meows."
- Create objects of both classes.
- Call the sound() method using both objects.
'''
class Dog:
    def sound(self):
        print("Dog barks.")

class Cat:
    def sound(self):
        print("Cat meows.")

dog1 = Dog()
dog1.sound()
cat1 = Cat()
cat1.sound()