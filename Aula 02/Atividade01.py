class Client:
    def __init__(self, id_client, name):
        self.id = id_client
        self.name = name
        
    def __eq__(self, other):
        if not isinstance(other, Client):
            return NotImplemented
        return self.id == other.id
    
#Uso
client1 = Client("001", "Ana Silva")
client2 = Client("001", "Ana Paula Silva")
client3 = Client("002", "Ana Paula Silva")
print(client1 == client2)
print(client2 == client3)