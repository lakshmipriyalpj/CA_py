class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def display(self):
        print("Student Information:")
        print("Name:", self.name)
        print("Grade:", self.grade)
        print("Age:", self.age)