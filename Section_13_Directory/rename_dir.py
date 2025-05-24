import os
# Rename Folder
# to work on this you need to create old path folder

old_path = os.path.join('Section_dir')
if not os.path.exists(old_path) or os.path.isdir(old_path):
    os.mkdir(old_path)
    print(f"The Folder Created -> {old_path}")

new_path = os.path.join('Section_new_dir')

if os.path.exists(old_path) and not os.path.isdir(new_path):
    os.rename(old_path,new_path)
    print(f"Folder Renamed -> {new_path}")
    print(f"Folder old path check -> {os.path.exists(os.path.join('Section_dir'))}")