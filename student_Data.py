#A python program consisting of 20 students name with their age, best subject, subject weakness and position.

Students = {
    "Stud1": {
    "name": "Daniel Godwin",
    "age": 15,
    "best_subject": "Mathematics",
    "subject_weakness": "Physics",
    "score": 95
    },
    "Stud2": {
    "name": "David Godwin",
    "age": 10,
    "best_subject": "English Language",
    "subject_weakness": "Cultural Science",
    "score": 70
    },
    "Stud3": {
    "name": "Mosope Ihejiawu",
    "age": 14,
    "best_subject": "Mathematics",
    "subject_weakness": "Biology",
    "score": 89
    },
    "Stud4": {
    "name": "Monachi Ihejiawu",
    "age": 12,
    "best_subject": "Mathematics",
    "subject_weakness": "History",
    "score": ""
    },
    "Stud5": {
    "name": "Zita Godwin",
    "age": 25,
    "best_subject": "Literature",
    "subject_weakness": "Mathematics",
    "score": 76
    },
    "Stud6": {
    "name": "Bella Godwin",
    "age": 12,
    "best_subject": "Biology",
    "subject_weakness": "Chemistry",
    "score": 90
    }
}

def showAll():
    print("The Total number is :", countStudent())
    for i in Students:
        print((Students[i]))

def showOnlyName():
    print("")
    for person in Students.values():
        print(person["name"])
def showOnlyAge():
    print("")
    for personAge in Students.values():
        print(personAge["age"])

def showOnlyBestSub():
    print("")
    for bestSubject in Students.values():
        print(bestSubject["best_subject"])


def showWeakSub():
    print("")
    for weakSubject in Students.values():
        print(weakSubject["subject_weakness"])

def countStudent():
    total = len(Students)
    print(total)

def AddNewStud(name, age, bestSub, subjectW, score):
    global Students

    student_key = "Stud" + str(len(Students)+1)

    new_student = {
        "name": name,
        "age": age,
        "bestSub": bestSub,
        "subjectW": subjectW,
        "score": score
    }

    Students[student_key] = new_student

    print(f"The name: {name} has been added to the Student Mgt")
     