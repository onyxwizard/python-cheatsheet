class Student:
    total_students = 0  # class-level attribute

    def __init__(self, name):
        self.name = name  # instance-level attribute
        Student.total_students += 1  # increase counter

    def introduce(self):
        print(f"Hi, I'm {self.name}!")

    @classmethod
    def student_count(cls):
        print(f"Total students: {cls.total_students}")

s1 = Student("Alice")
s2 = Student("Bob")

s1.introduce()  # Output: Hi, I'm Alice!
s2.introduce()  # Output: Hi, I'm Bob!

Student.student_count()  # Output: Total students: 2

s1.student_count()  # Still works! Output: Total students: 2