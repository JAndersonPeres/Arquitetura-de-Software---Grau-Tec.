from datetime import date
# MODEL
class Patient:
    def __init__(self, id:str, name:str, age:int, cpf:str):
        self.id = id
        self.name = name
        self.age = age
        self.cpf = cpf

class Doctor:
    def __init__(self, id:str, name:str, speciality:str):
        self.id = id
        self.name = name
        self.speciality = speciality

class Appointment:
    def __init__(self, id:str, patient:Patient, doctor:Doctor, tDate:date, value:float):
        self.id = id
        self.pacient = patient
        self.doctor = doctor
        self.date = tDate
        self.value = value
        self.payment = False

    def doPayment(self):
        self.payment = True

# SERVICE
class PatientService:
    def register(self, patient:Patient):
        print(f"Patient {patient.name} Registered!")

class AppointmentService:
    def booking(self, appointment:Appointment):
        print(f"Appointment booked for {appointment.pacient.name} with Dr. {appointment.doctor.name}")
    
    def approve(self, appointment:Appointment):
        if appointment.payment:
            print("Appointment Approved!")
        else:
            print("Cannot Approve Without Payment!")
    
class PaymentService:
    def pay(self, appointment:Appointment):
        appointment.doPayment()
        print("Payment confirmed!")

class NotificationService:
    def sendConfirmation(self, patient:Patient):
        print(f"Confimation Email sent to {patient.name}")

# CONTROLLER
class ClinicController:
    def __init__(self):
        self.patientService = PatientService()
        self.appointmentService = AppointmentService()
        self.paymentService = PaymentService()
        self.notificationService = NotificationService()

    def completeFlux(self):
        patient = Patient("P001","Mary Silva",35,"12345678900")
        doctor = Doctor("D001","Dr. John","Cardiology")
        appointment = Appointment("A001",patient,doctor,date.today,45.80)

        self.patientService.register(patient)
        self.appointmentService.booking(appointment)

        self.paymentService.pay(appointment)

        self.appointmentService.approve(appointment)

        self.notificationService.sendConfirmation(patient)