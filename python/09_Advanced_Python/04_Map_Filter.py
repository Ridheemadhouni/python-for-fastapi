'''
Write a Python program to:

- Create a list containing:
    1, 2, 3, 4, 5
- Use map() with a lambda function to calculate the square of each number.
- Convert the result into a list.
- Display the squared numbers.
'''
numbers = [1,2,3,4,5]
square = map(lambda x: x ** 2, numbers)
result = list(square)
print(result)
'''
Write a Python program to:

- Create a list containing:
    1, 2, 3, 4, 5, 6
- Use filter() with a lambda function to keep only even numbers.
- Convert the result into a list.
- Display the even numbers.
'''
even_num = filter(lambda x: x%2==0,numbers)
result2 = list(even_num)
print(result2)
