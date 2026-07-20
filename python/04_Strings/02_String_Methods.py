'''Write a Python program that takes a sentence from the user and prints:
Original string
Uppercase
Lowercase
Title case
Capitalized string
Total occurrences of the letter 'a'
Position of the first occurrence of 'a'
Whether the string starts with "Python"
Whether the string ends with "API"'''
string = input("Enter a sentence: ")
print("======= string information ======")
print("Original string:",string)
print("Uppercase:",string.upper())
print("Lowercase:",string.lower())
print("Title case:",string.title())
print("Capitalized string:",string.capitalize())
print("Total occurrences of the letter 'a':",string.count("a"))
print("Position of the first occurrence of 'a':",string.find("a"))
print("Whether the string starts with Python:",string.startswith("Python"))
print("Whether the string ends with API:",string.endswith("API"))
