import os
# If Folder doesn't exist then create one by

dir_path = os.path.join('Section_dir')

if not os.path.exists(dir_path) or os.path.isdir(dir_path):
    os.mkdir(dir_path)
    print(f"The Folder Created -> {dir_path}")
    