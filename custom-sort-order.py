
lst = ["abc", "aab", "a", "b", "d", "c"]

sorted_list = sorted(lst, key=lambda x: (len(x), x))

print(sorted_list)