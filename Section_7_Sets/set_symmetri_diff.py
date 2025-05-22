set_1 = {'A','B','C'}
set_2 = {'B','C','E'}

print("Set Symmetric Difference")
# use symmetric_difference() method or '^' Symmetric difference operator
# As Symmetric difference method we can use iterables but not with operator,
# methods have upper hand
print(set_1.symmetric_difference(set_2))
print(set_1.symmetric_difference([1,2,3]))
print(set_1 ^ set_2)
#print(set_1 ^ [1,2,3]) # This cause type Error