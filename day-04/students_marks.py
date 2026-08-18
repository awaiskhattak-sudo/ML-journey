students = {
    "Ali": 80,
    "Ahmed": 65,
    "Sara": 90,
    "Ayesha": 75
}

for student, marks in students.items():
    if marks >= 70:
        print(student.title(), marks)
