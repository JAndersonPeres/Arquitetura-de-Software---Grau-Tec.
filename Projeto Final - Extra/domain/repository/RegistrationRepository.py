from abc import ABC, abstractmethod
from model.Registration import Registration
class RegistrationRepository(ABC):
    @abstractmethod
    def save(self, registration:Registration): pass
    @abstractmethod
    def read(self): pass
    @abstractmethod
    def listAll(self): pass
    @abstractmethod
    def searchById(self, id:str): pass