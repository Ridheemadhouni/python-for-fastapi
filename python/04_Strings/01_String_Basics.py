'''Write a Python program that takes a string from the user and prints:

The complete string
Total number of characters
First character
Last character
Each character with its index'''
string = input("Enter a string: ")
print("String:",string)
print("Lenght:",len(string))
print("First character:",string[0])
print("Last character:",string[-1])
for i in range(len(string)):
    print("Character at index",i,":",string[i])