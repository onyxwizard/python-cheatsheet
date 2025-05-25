from pprint import pprint

class School:
    school_name = "NSN"
    

scool = School()

print(type(School)) # <class 'type'>
print(type(scool)) # <class '__main__.School'>
print(isinstance(scool,School)) # True

# Access class variables 
print(School.school_name)

# use getattr() to assign values to variables
use_get_attr = getattr(scool,'school_name')
print(use_get_attr)

# if no variable exist set a default value
use_get_attr = getattr(scool,'media','Oops! variable not found')
print(use_get_attr)

#Set values for class variables
set_attr = setattr(scool,'media','test') # create a new variable
set_attr1 = setattr(scool,'school_name','Zion') # update an existing variable
print(getattr(scool,'media'),getattr(scool,'school_name'))

#Delete class variables
# use delattr() or del key
delattr(scool,'media') # or del scool.media
#print(getattr(scool,'media'))

#Class variable storage 
class Test:
    sample = 1
    
    def render():
        print("Seen what is render using __dict__")
pprint(Test.__dict__)  #used pprint |  Output : <function Test.render at 0x000001FC450FB010>



