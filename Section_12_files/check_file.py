# Approach 1
from os.path import exists

file_path = exists('sample.txt')
print(file_path)

# Approach 2
from pathlib import Path

file_path2 = Path('sample.txt')
print(file_path2.is_file())