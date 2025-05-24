#open a file and write it
# use with to close file automatically

# Approach 1 - Manually close the file
lines = ['Readme', '\nHow to write text files in Python']
file = open('sample.txt','w')
file.writelines(lines)
file.close()

# Approach 2 - use with to Auto close the file
words = ['\nReadme', '\nHow to write text files in Python']
with open('sample.txt','a') as file:
    file.writelines(words)