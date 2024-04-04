#A python program consisting of 20 students name with their age, best subject, subject weakness and position.

Students = {
    "Stud1": {
    "name": "Daniel Godwin",
    "age": 15,
    "best_subject": "Mathematics",
    "subject_weakness": "Physics",
    "score": ""
    },
    "Stud2": {
    "name": "David Godwin",
    "age": 10,
    "best_subject": "English Language",
    "subject_weakness": "Cultural Science",
    "score": ""
    },
    "Stud3": {
    "name": "Mosope Ihejiawu",
    "age": 14,
    "best_subject": "",
    "subject_weakness": "",
    "score": ""
    },
    "Stud4": {
    "name": "Monachi Ihejiawu",
    "age": 12,
    "best_subject": "",
    "subject_weakness": "",
    "score": ""
    },
    "Stud5": {
    "name": "Zita Godwin",
    "age": 25,
    "best_subject": "Literature",
    "subject_weakness": "Mathematics",
    "score": ""
    },
    "Stud6": {
    "name": "Bella Godwin",
    "age": 12,
    "best_subject": "Biology",
    "subject_weakness": "Chemistry",
    "score": ""
    }
}

def showAll():
    for i in Students:
        print((Students[i]))

def showOnlyName():
    for person in Students.values():
        print(person["name"])

