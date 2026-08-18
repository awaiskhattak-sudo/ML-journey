marks = [80, 75, 90, 85, 70]

def calculate_average(marks):

    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    print("Total Marks:", total)
    print("Average Marks:", average)


calculate_average(marks)
