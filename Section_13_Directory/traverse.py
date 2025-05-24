import os

file_path = os.path.join('../')

# Actually traverse all folder and files
for root,dir,file in os.walk(file_path):
    print(f"{root}")
    print(f"{dir}")
    print(f"{file}")
    print('-' * 40)