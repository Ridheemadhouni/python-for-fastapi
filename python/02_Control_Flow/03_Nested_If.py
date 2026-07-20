#Check if a number is positive. If yes, check whether it is even or odd.
num = int(input("Enter a number: "))

if(num>0):
    if(num%2==0):
        print("The number is a positive even number.")
    else:
        print("The number is a positive odd number.")
elif(num==0):
    print("The number is zero.")
else:
    print("The number is  negative number.")

