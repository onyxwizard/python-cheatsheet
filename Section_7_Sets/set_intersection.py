set_1 = {'A','B','C'}
set_2 = {'C','D','E'}

print("Set Intersection")
# use intersection() method or '&' intersection operator
# As intersection method we can use iterables but not with operator,
# methods have upper hand
print(set_1.intersection(set_2))
print(set_1.intersection([1,2,3]))
print(set_1 & set_2)
#print(set_1 & [1,2,3]) # This cause type Error