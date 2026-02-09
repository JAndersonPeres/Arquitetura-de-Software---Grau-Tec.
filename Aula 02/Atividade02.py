class Price:
    def __init__(self, value:float, coin:str = "BRL"):
        if not isinstance(value, (int,float)) and value <= 0: raise ValueError("Value must be numeric or positive.")
        self.value = value
        self.coin = coin
        
    def __eq__(self, other):
        if not isinstance(other, Price): return NotImplemented
        return self.value == other.value and self.coin == other.coin
    
price1 = Price(100)
price2 = Price(200)
price3 = Price(100, "USD")
price4 = Price(100)

def chooseCoin(price: Price):
    if price.coin == "BRL": return "R$"
    return "$"

print(f"{chooseCoin(price1)} {price1.value:.2f} == {chooseCoin(price2)} {price2.value:.2f}: {price1 == price2}")
print(f"{chooseCoin(price1)} {price1.value:.2f} == {chooseCoin(price3)} {price3.value:.2f}: {price1 == price3}")
print(f"{chooseCoin(price1)} {price1.value:.2f} == {chooseCoin(price4)} {price4.value:.2f}: {price1 == price4}")