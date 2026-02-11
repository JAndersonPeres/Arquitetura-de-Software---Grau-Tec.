class Client:
    def __init__(self, idClient:str, name:str):
        self._id = idClient
        self._name = name
        
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    def introduce(self):
        print(f"Client: {self._name}")
        
class Request:
    def __init__(self, idRequest:str, client:Client, value:float):
        self._id = idRequest
        self._client = client
        self._value = value
    
    @property
    def id(self):
        return self._id
    
    @property
    def client(self):
        return self._client
    
    @property
    def value(self):
        return self._value
    
class RequestService:
    def createRequest(self, idRequest:str, client:Client, value:float):
        request = Request(idRequest, client, value)
        
        print("\nRequest Sucessfully Created!")
        print("Request's ID:", request.id)
        print("Client:", request.client.name)
        print(f"Value: R$ {request.value:.2f}")
        return request
        
client1 = Client("C001", "Mary")
client1.introduce()
print("-----------------------")
service = RequestService()
request = service.createRequest("P001", client1, 150)