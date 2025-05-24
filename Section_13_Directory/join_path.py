import os

'''
    joins path components together and returns a path 
                with the corresponding path separator
'''

fp = os.path.join("../",'Section_5_List')
print(os.getcwd())
os.chdir(fp)
print(os.getcwd())

fp = os.path.split(fp) # To get back use split
print(fp)