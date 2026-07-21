'''
Write a Python program to:

- Open a file named "student.txt" in read mode.
- Read and display its contents.
- Close the file after reading.
'''
file = open("python/07_File_Handling/student.txt","r")
content = file.read()
print(content)
file.close()