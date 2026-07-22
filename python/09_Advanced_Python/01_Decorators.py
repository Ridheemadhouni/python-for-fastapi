'''
Write a Python program to:

- Create a decorator named message.
- Inside the decorator:
    - Print "Program Started".
    - Call the original function.
    - Print "Program Ended".
- Create a function named display() that prints:
    "Welcome to Python Decorators."
- Apply the decorator using @message.
- Call the display() function.
'''
def decorator(func):
    def inside():
        print("Program Started.")
        func()
        print("Program ended.")
    return inside

@decorator
def display():
    print("Welcome to Python Decorators.")
display()

