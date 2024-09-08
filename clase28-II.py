class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID IS: {self.student_id}")

student = Student("Juan", 26, "1002")
student.introduce()
