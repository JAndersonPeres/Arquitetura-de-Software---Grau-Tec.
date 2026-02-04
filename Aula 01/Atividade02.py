class Animal:
    def __init__(self, name:str):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")
    
    def eat(self):
        print(f"{self.name} is devouring the food.")
        
rex = Dog("Rex")
rex.eat()
rex.sleep()
rex.bark()
print(type(rex))