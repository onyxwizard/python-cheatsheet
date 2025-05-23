#open a file and read it
# use with to close file automatically

# Approach 1
file = open('sample.txt')
print(file.readline())
file.close()

# Approach 2
with open('sample.txt') as file:
    for line in file:
        print(line.strip())