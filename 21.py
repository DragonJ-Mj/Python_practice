# Problem: Given a list with duplicate elements, use a for loop to build a new list that contains each element exactly once (preserving the original order). Do not use set().
# ​Given: dupes = ['a', 'b', 'a', 'c', 'b', 'd']
# ​Expected Output List: ['a', 'b', 'c', 'd']


dupes = ['a', 'b', 'a', 'c', 'b', 'd']
new = []
for i in dupes:
    if (i not in new):
        new.append(i)
print(new)