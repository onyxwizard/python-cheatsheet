import os

file = os.path.exists('test.txt')
if not file:
    with open('test.txt','x') as file:
        print("File is created")
        file.write("Success")

with open('test.txt','r') as file:
        for line in file:
            print(line)

print('File Renamed to sample')
os.rename('test.txt','sample.txt')