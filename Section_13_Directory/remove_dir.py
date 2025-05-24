import os

file_path = os.path.join('Section_new_dir')

if os.path.exists(file_path) or os.path.isdir(file_path):
    os.rmdir(file_path)
    print(file_path + ' is removed.')