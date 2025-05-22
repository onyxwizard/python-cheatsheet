set_1 = {'A','B','C'}
set_2 = {'C','D','E'}

print("Set Union")
# use Union() method or '|' union operator
# As union method we can use iterables but not with operator,
# methods have upper hand
print(set_1.union(set_2))
print(set_1.union([1,2,3]))
print(set_1|set_2)
#print(set_1 | [1,2,3]) # This cause type Error