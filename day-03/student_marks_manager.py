student1 = [85, 72, 90]
student2 = [65, 88, 76]
student3 = [92, 79, 84]

all_marks = student1 + student2 + student3

print(all_marks)

print(all_marks[0])
print(all_marks[8])

for marks in all_marks:
    if marks > 80:
        print(marks)

print(max(all_marks))
print(min(all_marks))
print(sum(all_marks))
print(len(all_marks))

all_marks.sort()
print(all_marks)

average = sum(all_marks) / len(all_marks)

if average >= 80:
    print("Good Performance")
else:
    print("Need Improvement")
