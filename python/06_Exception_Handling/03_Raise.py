'''
Write a Python program to:

- Take the user's age as input.
- If the age is less than 18, raise a ValueError with the message:
  "Age must be 18 or above."
- Otherwise display:
  "You are eligible."
'''

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("Eligible")
except ValueError as e:
    print(e)
