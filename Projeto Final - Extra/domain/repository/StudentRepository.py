from abc import ABC, abstractmethod
from model.Student import Student
class StudentRepository(ABC):
    @abstractmethod
    def save(self, student:Student): pass
    @abstractmethod
    def read(self): pass
    @abstractmethod
    def listAll(self): pass
    @abstractmethod
    def searchById(self, id:str): pass