list1 = [1,2,3,4,5]
list2 = [2,4,6]

intersect = filter(lambda x: x in list1, list2)

print(list(intersect))