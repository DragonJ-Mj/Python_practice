# zip()

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
grades = ['A', 'B', 'C']

for name, age, grade in zip(names, ages, grades):
    print(f"{name} is {age} years old and has a grade of {grade}.")

