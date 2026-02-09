class Client:
    def __init__(self, id_client:str, name:str):
        self.id = id_client
        self.name = name
        
    def __eq__(self, other):
        if not isinstance(other, Client):
            return NotImplemented
        return self.id == other.id
    
class Price:
    def __init__(self, value, coin="BRL"):
        if not isinstance(value, (int,float)) or value <= 0:
            raise ValueError("Value must be numeric or positive.")
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
    
book_price = Price(59.90)
other_price = Price(59.90)
new_price = Price(49.90)
print(book_price == other_price)
print(book_price == new_price)
print(hash(book_price))
print(hash(other_price))
print(hash(new_price))