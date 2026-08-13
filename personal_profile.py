name = input("Enter your name: ")
age = int(input("Enter your age: "))
cityname = input("Enter your cityname: ")
Degreename = input("Enter your Degreename: ")
skill = input("Enter your skill: ")

name = name.strip().title()
cityname = cityname.strip().title()
Degreename = Degreename.strip().title()
skill = skill.strip().title()

introduction = f"My name is {name} and I am {age} years old. I am from {cityname}. I completed my graduation in {Degreename} and I am proficient in {skill}."

print(introduction)
