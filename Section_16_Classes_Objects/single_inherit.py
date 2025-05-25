class Student:
    
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Student Name is |{self.name}|\nStudent age is |{self.age}|\n"
    
class Course(Student):
    
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course = course
    
    def greet(self):
        return super().greet() + f"Student Enrolled in |{self.course}|"
    
print(Course.__mro__)
# student1 = Course("Alice",25,"Computer Science")
# print(student1.greet())
    
    