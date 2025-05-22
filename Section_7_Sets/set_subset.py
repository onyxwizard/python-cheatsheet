set_1 = {'A','B','C'}
set_2 = {'A','B','C','E','F'}

print("Set Subset")

print(set_1.issubset(set_2))
print(set_1.issubset([1,2,3]))
print(set_1 <= set_2) # checks subset
print(set_1 < set_2) # checks Proper subset