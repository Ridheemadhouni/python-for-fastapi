'''
Write a Python program to:

- Create a list containing:
    10, 20, 30
- Convert the list into an iterator using iter().
- Print each element using next().
'''
lists = [10,20,30]
it = iter(lists)
print(next(it))
print(next(it))
print(next(it))