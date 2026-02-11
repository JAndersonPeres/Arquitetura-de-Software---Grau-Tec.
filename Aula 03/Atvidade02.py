class Product:
    def __init__(self, id:str, name:str, price:float):
        self._id = id
        self._name = name
        self._price = price
        
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
class ProductService:
    def __init__(self):
        self._products = []
        
    def createProduct(self, product:Product):
        self._products.append(product)
        print(f"Product({product.id}) Sucessfully Created!")
        return product
    
    def listAll(self):
        print("---------------------------------")
        for p in self._products:
            print("ID:", p.id)
            print("Name:", p.name)
            print(f"Price: R$ {p.price:.2f}")
            print("---------------------------------")
    
product1 = Product("P001", "Wireless Mouse", 85.50)
product2 = Product("P002", "Wireless Keyboard", 125.63)
product3 = Product("P003", "Bluetooth Headset", 75.89)
product4 = Product("P004", "PlayStation GamePad", 65.42)
service = ProductService()
service.createProduct(product1)
service.createProduct(product2)
service.createProduct(product3)
service.createProduct(product4)
service.listAll()