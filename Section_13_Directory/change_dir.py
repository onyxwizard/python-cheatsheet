import os

# Current working Directory
cwd = os.getcwd()
print(f'Current Directory pointing to -> {cwd}')

os.chdir('../../') # Helps to move forward and backward of current Dir

cwd = os.getcwd()
print(f'Current Directory pointing to -> {cwd}')