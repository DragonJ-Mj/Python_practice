#### Map Function

##map(function, iteration)

#square
number = [1,2,3,4,5]
sq= list(map(lambda x : x**2, number))
print(sq)


##even number

even_num = list(map(lambda x: x%2==0, [1,2,3,4,5,6,7,8,9]))
print(even_num)