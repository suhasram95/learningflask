from statistics import median
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = (90, 90, 93, 78, 90)
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    def student_median(self):
        return median(self.grades)

student = Student("Bob")
print (student.name)
print (student.grades)
print (student.average_grade())
print (student.student_median())