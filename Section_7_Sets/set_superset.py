set_1 = {'A','B','C','E','F'}
set_2 = {'A','B','C'}

print("Set Superset")

print(set_1.issuperset(set_2))
print(set_1.issuperset([1,2,3]))
print(set_1 >= set_2) # checks superset
print(set_1 > set_2) # checks Proper superset