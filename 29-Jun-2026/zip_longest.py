# zip_longest()

from itertools import zip_longest

## define two lists of different lengths
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30]

## use zip_longest to combine the lists
for name, age in zip_longest(names, ages, fillvalue='N/A'):
    print(f"{name} is {age} years old.")
