#Create a function that prints student details. Default course should be "BCA".
def student_detail(name="ridhi",course ="BCA",age = 23,cgpa=9.0):
    print("Name:",name)
    print("Course:",course)
    print("Age: ",age)
    print("CGPA: ",cgpa)

student_detail()
student_detail("khushi","Btech",24)
student_detail("abhi","Btech",24,9.5)