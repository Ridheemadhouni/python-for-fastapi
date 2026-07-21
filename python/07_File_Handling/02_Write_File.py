'''- Create or open a file named "student.txt" in write mode.
- Write the following details into the file:

  Name: Ridhima
  Course: BCA
  College: IITM

- Close the file.
- Display the message:
  "Data written successfully."
'''
file = open("python/07_File_Handling/student.txt","w")
file.write("Name: Ridhima\nCourse: BCA\nCollege: IITM")
file.close()
print("Data written successfully.")
file = open("python/07_File_Handling/student.txt","r")
view = file.read()
print(view)
file.close()