import math
from statistics import mean


class CalculateAverageMixin:
    def get_average(self, data):
        return math.floor(mean(data))

class Student(CalculateAverageMixin):
    def __init__(self, name, age, grades=[]):
        self.name = name
        self.age = age
        self.grades = grades
class Employee(CalculateAverageMixin):
    def __init__(self, name, age, daily_working_hours=[]):
        self.name = name
        self.age = age
        self.daily_working_hours = daily_working_hours

student = Student("Maria", 20, [5,6])
teacher = Employee("Gosho", 25, [10,17])
print(student.get_average(student.grades))
print(teacher.get_average(teacher.daily_working_hours))



