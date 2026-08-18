students = {
    "Ali": 80,
    "Ahmed": 65,
    "Sara": 90,
    "Ayesha": 75
}

total_marks = 0

for marks in students.values():
    total_marks += marks

average = total_marks / len(students)

print("Average:", average)

for student, marks in students.items():
    if marks > average:
        print(student, marks)
