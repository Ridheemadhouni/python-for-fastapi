'''
Write a Python program to:

- Create two lists:
    Names: "Ridhima", "Rahul", "Priya"
    Marks: 90, 85, 95
- Use zip() to combine both lists.
- Display each student's name and marks.
'''
names = ["Ridhima", "Rahul", "Priya"]
marks = [90, 85, 95]

for name,mark in zip(names,marks):
    print(name,":",mark)

'''
Write a Python program to:

- Create a list:
    "Python", "FastAPI", "PostgreSQL"
- Use enumerate() to display the index and course name.
'''
courses = ["Python", "FastAPI", "PostgreSQL"]

for index,course in enumerate(courses):
    print(index,":",course)