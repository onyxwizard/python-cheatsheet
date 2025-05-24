import os

dir_path = os.path.join('../','Section_5_List')

if os.path.exists(dir_path) or os.path.isdir(dir_path):
    print(f"The Folder Exist -> {dir_path}")
