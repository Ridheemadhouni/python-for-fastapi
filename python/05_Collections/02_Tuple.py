'''Write a Python program to:

- Create a student tuple.
- Print the first element, last element, length, first 2 elements and reversed tuple.
- Unpack the tuple into variables.
- Create a marks tuple and print the maximum marks, total marks and count of 95.'''
student = ("ridhi","Ridheema","Abhi","Ajay","Khushi")
print("The first element:",student[0])
print("The last element:",student[-1])
print("The Length:",len(student))
print("The first 2 element:",student[:2])
print("The reverse of tuple:",student[::-1])
name1,name2,name3,name4,name5 = student
print("===============================")
print("Tuple into variables:")
print(name1)
print(name2)
print(name3)
print(name4)
print(name5)
print("===============================")
marks = (95,66,84,95,78)
print("Maximum of marks:",max(marks))
print("Total marks:",sum(marks))
print("Count of 95:",marks.count(95))