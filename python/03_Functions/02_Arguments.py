#Create a function that prints the greater of two numbers.
def greater_number(num1,num2):
    if num1>num2:
        print("The greater number is:",num1)
    elif num1==num2:
        print("Both number are equal:",num1,"=",num2)
    else:
        print("The greater number is:",num2)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

greater_number(num1,num2)
