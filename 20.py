# use a for loop to find and print the largest number in a list.
# ​Given: scores = [45, 82, 94, 12, 75, 63]



scores = [45, 82, 94, 12, 75, 63]
largest = scores[0]
for i in scores:
    if i > largest:
        largest = i
print(largest)
