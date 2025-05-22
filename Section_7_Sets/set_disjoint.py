set_1 = {'A','B','C','E','F'}
set_2 = {'A','B','C'}

print("Set Disjoint set")
# There should be no intersection of elements means set 1 and set 2 needs to be unique
print(set_1.isdisjoint(set_2))
print(set_1.isdisjoint([1,2,3]))
# disjoint has no operator
