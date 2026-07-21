'''
Write a Python program to:

- Open the file "student.txt" in append mode.
- Add the following line to the file:

  City: New Delhi

- Close the file.
- Display the message:
  "Data appended successfully."
'''

file = open("python/07_File_Handling/student.txt","a")
file.write("\nCity: New Delhi")
file.close()
print("Data appended successfully.")