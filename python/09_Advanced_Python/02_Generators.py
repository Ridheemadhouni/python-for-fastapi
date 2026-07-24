'''
Write a Python program to:

- Create a generator function named numbers().
- Use the yield keyword to generate:
    1
    2
    3
- Create a generator object.
- Print all generated values using a for loop.
'''
def numbers():
    yield 1
    yield 2
    yield 3

num = numbers()

for i in num:
    print(i)