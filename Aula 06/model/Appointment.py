from Pacient import Pacient
from Doctor import Doctor
from datetime import date

class Appointment:
    def __init__(self, id:str, pacient:Pacient, doctor:Doctor, tDate:date, value:float):
        self.id = id
        self.pacient = pacient
        self.doctor = doctor
        self.date = tDate
        self.value = value
        self.payment = False

    def doPayment(self):
        self.payment = True