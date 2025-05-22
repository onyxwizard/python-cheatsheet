set_1 = {'A','B','C'}
set_2 = {'B','C','E'}

print("Set Difference")
# use Difference() method or '-' difference operator
# As difference method we can use iterables but not with operator,
# methods have upper hand
print(set_1.difference(set_2))
print(set_1.difference([1,2,3]))
print(set_1 - set_2)
#print(set_1 - [1,2,3]) # This cause type Error