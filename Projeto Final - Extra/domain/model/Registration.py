from Student import Student
from Course import Course
class Registration:
    def __init__(self, id:str, student:Student, course:Course):
        self.id = id
        self.student = student
        self.course = course
        self.payment = False
    
    def doPay(self):
        self.payment = True