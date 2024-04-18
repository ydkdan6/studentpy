import student_Data

result = student_Data

result.countStudent()

name = input("Enter Name: ")
age = input("Enter Age: ")
bestSub = input("Enter Best Subject: ")
subjectW = input("Enter Subject Weakness: ")
score = input("Enter Score: ")

result.AddNewStud(name, age, bestSub, subjectW, score)

result.showAll()