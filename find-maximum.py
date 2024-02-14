lst = [1,2,3,4,5]

maximum = lambda x,y: y if x < y else x

def max_num(lst, func):
    highest = lst[0]
    for num in lst:
        highest = func(highest,num)
    return highest

print(max_num(lst,maximum))
