'''Write a Python program that takes a string from the user and prints:

Original string
First 3 characters
Last 3 characters
String except the first character
String except the last character
Every second character
Reversed string'''
string = input("Enter a string: ")
print("========= String Information =========")
print("Original string:",string[:])
print("First 3 characters:",string[:3])
print("Last 3 characters:",string[-3:])
print("String except the first character:",string[1:])
print("String except the last character:",string[:-1])
print("Every second character:",string[::2])
print("Reversed string",string[::-1])