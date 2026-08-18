students = {
    "Ali": 80,
    "Ahmed": 65,
    "Sara": 90,
    "Ayesha": 75
}

name = input("Enter your name: ").strip().title()

if name in students:
    print(name, students[name])
else:
    print("User not found")
