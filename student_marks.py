math = int(input("Enter your math marks: "))
physics = int(input("Enter your physics marks: "))
urdu = int(input("Enter your urdu marks: "))
English = int(input("Enter your English mark: "))

totalmarks = math + physics + English + urdu
average = totalmarks / 4

print(f"Math marks: {math}")
print(f"English marks: {English}")
print(f"Physics marks: {physics}")
print(f"Urdu marks: {urdu}")
print(f"Total marks: {totalmarks}")
print(f"Average: {average}")
