class Smartphone: # Class Creation
    
    Counter = 0 #class Attribute. It can be access all classes
    
    def __init__(self,model,type):
        # Two attributes are accessed across all class instance
        self.model = model # instance attribute 1
        self.type = type # instance attribute 2
        Smartphone.Counter += 1
        
    def features(self): # Instance method
        print("Available soon!")

print(Smartphone.Counter) # Counter is 0

smart = Smartphone(None,None) #  instance of a class
print(Smartphone.Counter) # Counter is 1
smart.model,smart.type = "Honor","Android"
print(smart.model,smart.type)