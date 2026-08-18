students = {
    "Ali": 85,
    "Ahmed": 72,
    "Awais": 91,
    "Usman": 63
}

def student_grade(students):

    for name, marks in students.items():

        if marks >= 80:
            print(name, marks, "- Grade A")

        elif marks >= 70:
            print(name, marks, "- Grade B")

        elif marks >= 60:
            print(name, marks, "- Grade C")

        else:
            print(name, marks, "- Grade F")


student_grade(students)
