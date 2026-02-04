class Person:
    def __init__(self, name:str):
        self._name = name
        
    def talk(self):
        print(f"Hi, my name is {self._name}")
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, newName:str):
        if (newName.replace(" ", "") != ""):
            self._name = newName
        else:
            raise ValueError("Invalid Name!")
            
p = Person("Anderson")
p.talk()

print(p.name)
try:
    p.name = input("Enter new name: ")
except ValueError as e:
    print(f"Error: {e}")
    
p.talk()