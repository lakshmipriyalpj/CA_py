from Student import Student


class School(Student):
    def school_student_display(self):
        print("School Student Information:")
        print("Name:", self.name)
        print("Grade:", self.grade)
        print("Age:", self.age)

# Create an instance of the Student class
student1 = Student("Priya", "10th", 14)

# Display student1's information using the display() method
student1.display()

# Create an instance of the School class
school_student1 = School("John", "12th", 17)

# Display school_student1's information using the school_student_display() method
school_student1.school_student_display()