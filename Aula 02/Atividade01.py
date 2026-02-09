class Client:
    def __init__(self, id_client:str, name:str, email: str):
        self.id = id_client
        self.name = name
        self.email = email
        
    def __eq__(self, other):
        if not isinstance(other, Client):
            return NotImplemented
        return self.id == other.id
    
class Price:
    def __init__(self, value, coin="BRL"):
        if not isinstance(value, (int,float)) or value <= 0:
            raise ValueError("Value must be numeric and positive.")
        self._value = value
        self._coin = coin
        
    @property
    def value(self):
        return self._value
    
    @property
    def coin(self):
        return self._coin
    
    def __eq__(self, other):
        if not isinstance(other, Price):
            return NotImplemented
        return self.value == other.value and self.coin == other.coin
    
    def __hash__(self):
        return hash((self.value, self.coin))
    
class Product:
    def __init__(self, id_product:str, name:str, price:Price):
        self.id = id_product
        self.name = name
        self.price = price
        
class ItemRequest:
    def __init__(self, product:Product, quantity:int):
        self.product = product
        self.quantity = quantity
        self.total = product.price.value * quantity
        
class Request:
    def __init__(self, id_request:str, client:Client):
        self.id = id_request
        self.client = client
        self.items = []
        self.status = "IN PROGRESS..."
        
    def add_items(self, product:str, quantity:int):
        item = ItemRequest(product, quantity)
        self.items.append(item)
        
    def calculate_total(self):
        return sum(item.total for item in self.items)
    
client_ana = Client("C001", "Ana Silva", "ana@email.com")
product_book = Product("P001", "Clean Code", Price(85.00))
product_mouse = Product("P002", "Wireless Mouse", Price(120.00))
product_headset = Product("P003", "Wireless Headset", Price(85.50))
product_hardDrive = Product("P004", "Hard Drive - 256GB", Price(56.70))
product_keyboard = Product("P005", "Wireless Keyboard", Price(95.90))

request_ana = Request("REQ001", client_ana)
request_ana.add_items(product_book, 3)
request_ana.add_items(product_mouse, 2)
request_ana.add_items(product_headset, 1)
request_ana.add_items(product_hardDrive, 5)
request_ana.add_items(product_keyboard, 1)

print(f"{client_ana.name}'s Request Total: R$ {request_ana.calculate_total():.2f}")