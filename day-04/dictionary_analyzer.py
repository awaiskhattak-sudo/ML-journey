students = {
    "Ali": 80,
    "Ahmed": 65,
    "Sara": 90,
    "Ayesha": 75
}

print("Total students:", len(students))

highest_marks = 0
top_student = ""

for student, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        top_student = student

print("Highest marks:", highest_marks)
print("Top student:", top_student)

for student, marks in students.items():
    if marks >= 70:
        print(student, marks)
