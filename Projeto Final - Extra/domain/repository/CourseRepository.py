from abc import ABC, abstractmethod
from model.Course import Course
class CourseRepository(ABC):
    @abstractmethod
    def save(self, course:Course): pass
    @abstractmethod
    def read(self): pass
    @abstractmethod
    def listAll(self): pass
    @abstractmethod
    def searchById(self, id:str): pass