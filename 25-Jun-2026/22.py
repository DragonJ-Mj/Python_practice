# Problem: Given a list of numbers, use a for loop to create a new list that contains the squares of only the odd numbers from the original list.
# ​Given: numbers = [1, 2, 3, 4, 5]
# ​Expected Output List: [1, 9, 25] (since 1^2 = 1, 3^2 = 9, 5^2 = 25)


numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    if n % 2 == 1: 
        squares.append(n ** 2)
print(squares)