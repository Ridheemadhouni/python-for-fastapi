'''
Write a Python program to:

- Import the json module.
- Create a dictionary with:
    Name: "Ridhima"
    Course: "BCA"
    College: "IITM"
- Convert the dictionary into a JSON string using json.dumps().
- Display the JSON string.
'''
import json

student = {
     "Name" :"Ridhima",
     "Course" :"BCA",
     "College" : "IITM"
}
json_data = json.dumps(student)
print(json_data)
'''
Write a Python program to:

- Import the json module.
- Create the following JSON string:

  {"Name": "Rahul", "Age": 21, "Course": "BCA"}

- Convert the JSON string into a Python dictionary using json.loads().
- Display the dictionary.
- Display only the student's name using the dictionary.
'''
student2 = '{"Name": "Rahul", "Age": 21, "Course": "BCA"}'

python_data = json.loads(student2)
print(python_data)
print("Student name:",python_data["Name"])