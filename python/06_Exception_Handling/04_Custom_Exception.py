'''
Write a Python program to:

- Create a custom exception class named AgeError.
- Take the user's age as input.
- If the age is less than 18, raise AgeError with the message:
  "You must be 18 or older."
- Otherwise display:
  "Access Granted."
'''
class AgeError(Exception):
    pass
try:
    age = int(input("Enter your age: "))
    if age <18:
        raise AgeError("You must be 18 or order")
    print("Access Granted.")
except AgeError as e:
    print(e)