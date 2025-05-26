# what is self in python
class Student:
    
    def __init__(): # self is just a naming convention
        #self.attr = attributes
        pass

# Lets decode how self works
# This actually creates self meaning Obj variable is passed in  self place as argument
Obj = Student() 

'''
we get error : Obj = Student() 
TypeError: Student.__init__() takes 0 positional arguments but 1 was given
this is because when we create an object of instance class
the object is automatically passed as an argument this happens under the hood
'''
# lets see visually

obj = Student.__new__(Student)
Student.__init__(obj,'attribute')
print(obj.attr)