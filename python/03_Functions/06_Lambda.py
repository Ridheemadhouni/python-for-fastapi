#Create a lambda function to calculate the cube of a number.
cube = lambda num: num*num*num

num= int(input("Enter a number: "))

print("Cube of a number:",cube(num))