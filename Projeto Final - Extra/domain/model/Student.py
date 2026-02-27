from datetime import date
class Student:
    def __init__(self, id:str, name:str, cpf:str, birthDate:date):
        self.id = id
        self.name = name
        self.cpf = cpf
        self.birthDate = birthDate