# Sorted Function

sort_num = [1,2,3,4,5,6,7,8,9,10]
print(sorted(sort_num, reverse=True))


fruits = ["banana", "apple", "cherry", "date"]
print(sorted(fruits, reverse=True))


list1 = [("John", 25), ("Alice", 30), ("Bob", 20)]
# Sort by age (second element of the tuple)
sorted_list = sorted(list1, key=lambda x: x[1],reverse=True)
print(sorted_list)  
