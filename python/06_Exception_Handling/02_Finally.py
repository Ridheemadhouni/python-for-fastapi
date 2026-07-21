"""
File Name : 02_Finally.py
Topic     : Finally Block
"""

# ==========================================
#           Q1. Basic Finally
# ==========================================

'''
Write a Python program to:

- Print "Program Started".
- Use a try block to print "Inside Try Block".
- Use a finally block to print "Program Ended".
'''
print("=============== Basic Finally ==========================")
try:
    print("Program started")
    print("Inside try block")
finally:
    print("Program ended")
print("========================================================")
# ==========================================
# Q2. Finally with ZeroDivisionError
# ==========================================

'''
Write a Python program to:

- Take two integers as input.
- Divide the first number by the second number.
- Handle ZeroDivisionError.
- Use a finally block to display "Execution Completed".
'''
print("=============== Finally with ZeroDivisionError ==========================")
try:
    num1 = int(input("enter a first number: "))
    num2 = int(input("enter a second number: "))
    result = num1/num2
    print("Result:",result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution Completed")
print("========================================================")

# ==========================================
# Q3. Finally with ValueError
# ==========================================

'''
Write a Python program to:

- Take the user's age as input.
- Handle ValueError if the input is invalid.
- Use a finally block to print "Thank you for using the program."
'''
print("=============== Finally with ValueError ==========================")
try:
    age = int(input("Enter your age: "))
    print("Your age:",age)
except ValueError:
    print("Invalid input")
finally:
    print("Thank you for using the program.")
print("========================================================")

# ==========================================
# Q4. Finally with File Handling
# ==========================================

'''
Write a Python program to:

- Open a text file using try block.
- Read and display its contents.
- Handle FileNotFoundError if the file does not exist.
- Use finally block to print "File operation completed."
'''
print("=============== Finally with File Handling ==========================")
try:
    file = open("student.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("the file does not exist!!")
finally:
    file.close()
    print("File operation completed.")
print("========================================================")

# ==========================================
# Q5. Finally with Calculator
# ==========================================

'''
Write a Python program to:

- Take two numbers and an operator (+, -, *, /).
- Perform the selected operation.
- Handle:
    * ValueError
    * ZeroDivisionError
- Use a finally block to print "Calculator closed."
'''
print("=============== Finally with Calculator ==========================")
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        print("Result:", num1 / num2)

    else:
        print("Invalid operator!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter valid numbers.")

except Exception as e:
    print("Error:", e)
finally:
    print("Calculator closed.")
print("========================================================")

# ==========================================
# Q6. Login System 
# ==========================================

'''
Write a Python program to:

- Ask the user to enter a username and password.
- If the username is "admin" and the password is "1234",
  display "Login Successful".
- Otherwise display "Invalid Credentials".
- Use a finally block to print "Login process completed."
'''
print("=============== Login System  ==========================")
try:
    username = input("Enter username: ")
    password = int(input("Enter password: "))
    if username == 'admin' and password == 1234:
        print("Login Successful.")
    else:
       print("Invalid Credentials.")
finally:
    print( "Login process completed.")
print("========================================================")
