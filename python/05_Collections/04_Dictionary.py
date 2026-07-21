'''Write a Python program to:

- Create a student dictionary containing name, age, course and CGPA.
- Print the student's name and course.
- Update the age.
- Add the college name.
- Print all keys, values and key-value pairs.
- Remove the course.
- Print the total number of items in the dictionary.'''
Student_data = {
       "name":"ridhi",
        "age": 18,
        "course" : "BCA",
        "CGPA" : 9.0
}
print("Student data:",Student_data)
print("===================================================")
print("Student name:",Student_data.get("name"))
print("Course:",Student_data.get("course"))
Student_data["age"] = 20
print("Student Update data:",Student_data)
Student_data["college"] ="IITM college "
print("ADD college name in student data:",Student_data)
Student_data.pop("course")
print("Remove course from student data:",Student_data)
print("The total number of item in student data:",len(Student_data))
print("=========== Keys ===========")
for key in Student_data.keys():
    print(key)

print("=========== Values ===========")
for value in Student_data.values():
    print(value)

print("======= Key : Value =======")
for key, value in Student_data.items():
    print(key, ":", value)