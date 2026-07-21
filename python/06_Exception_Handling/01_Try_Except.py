# ==========================================
# Q1. Basic Try-Except
# ==========================================
'''
Write a Python program to:

- Take an integer input from the user.
- Print the entered number.
- If the user enters an invalid value, display "Invalid input!" using try-except.
'''
print("============== Basic Try-Except ==============")
try:
    age = int(input("Enter your age: "))
    print("Your age:",age)
except:
    print("Invalid input!")
print('=================================================')
# ==========================================
# Q2. ZeroDivisionError Handling
# ==========================================
'''
Write a Python program to:

- Take two integers as input from the user.
- Divide the first number by the second number.
- Handle ZeroDivisionError if the second number is 0.
- Display an appropriate error message.
'''
print("============== ZeroDivisionError Handling ==============")
try:
    num1 = int(input("Enter a first number: "))
    num2 = int(input("enter a second number: "))
    result = num1/num2
    print("The result is:",result)
except ZeroDivisionError:
     print("Cannot divide by zero!")
print('=================================================')
# ==========================================
# Q3. ValueError Handling
# ==========================================

'''
Write a Python program to:

- Take the user's age as input.
- Print the entered age.
- Handle ValueError if the user enters a non-numeric value.
'''
print("============== ValueError Handling ==============")
try:
    AGE = int(input("Enter your age: "))
    print("Your age is:",AGE)
except ValueError:
    print("Please enter a valid age.")
print('=================================================')
# ==========================================
# Q4. Exception as e
# ==========================================

'''
Write a Python program to:

- Create a list containing three numbers.
- Take an index as input from the user.
- Print the element at that index.
- Handle any exception using "Exception as e".
- Display the actual error message.
'''
print("============== ValueError Handling ==============")
number = [20,45,89]
try:
    index = int(input("Enter index number(0-2): "))
    print("Element:",number[index])
except Exception as e:
    print("Error:",e)
print('=================================================')
# ==========================================
# Q5. Calculator using Try-Except
# ==========================================

'''
Write a Python program to:

- Take two integers as input.
- Take an operator (+, -, *, /) from the user.
- Perform the selected operation.
- Handle:
    * ValueError
    * ZeroDivisionError
    * Any other unexpected exception
- Display appropriate messages for each case.
'''
print("============== Calculator using Try-Except ==============")
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
print('=================================================')
# ==========================================
# Q6. Student Percentage Calculator
# ==========================================

'''
Write a Python program to:

- Take marks of five subjects from the user.
- Calculate the total marks.
- Calculate the percentage.
- Handle ValueError for invalid inputs.
- Handle any unexpected exception using "Exception as e".
'''
print("============== Student Percentage Calculator ==============")
try:
    english = float(input("Enter English marks: "))
    maths = float(input("Enter Maths marks: "))
    science = float(input("Enter Science marks: "))
    computer = float(input("Enter Computer marks: "))
    hindi = float(input("Enter Hindi marks: "))

    total = english + maths + science + computer + hindi
    percentage = total / 5

    print("Total Marks:", total)
    print("Percentage:", percentage)

except ValueError:
    print("Please enter valid marks.")

except Exception as e:
    print("Error:", e)
print('=================================================')