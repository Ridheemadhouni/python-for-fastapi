#Find the factorial of a number using recursion.
def factorial(num):
    if(num == 0):
        return 1
    return num*factorial(num-1)
num = int(input("Enter a number: "))
print("Factorial of",num,"is:",factorial(num))