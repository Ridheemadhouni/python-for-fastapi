'''
Write a Python program to:

- Open the file "student.txt" using the with statement.
- Read and display its contents.
- Do not use file.close().
- Display the message:
  "File closed automatically."
'''
with open("python/07_File_Handling/student.txt",'r') as file:
    content = file.read()
    print(content)
