students = {
    "Ali": 85,
    "Ahmed": 72,
    "Awais": 91,
    "Usman": 63
}


def display_students(students):

    print("Students:")

    for name, marks in students.items():
        print(name, ":", marks)


def calculate_average(students):

    total = 0

    for name, marks in students.items():
        total += marks

    average = total / len(students)

    print("Average Marks:", average)


def highest_marks(students):

    highest = 0
    highest_student = ""

    for name, marks in students.items():

        if marks > highest:
            highest = marks
            highest_student = name

    print("Highest Marks:")
    print(highest_student, ":", highest)


display_students(students)

print()

calculate_average(students)

print()

highest_marks(students)
