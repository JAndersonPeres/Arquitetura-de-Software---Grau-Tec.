class RequestModel:
  def __init__(self, value:float):
    self.value = value

class Shipping:
  def __init__(self, value:float):
    self.value = value

class NormalShipping(Shipping):
  def __init__(self):
    super().__init__(20)

class ExpressShipping(Shipping):
  def __init__(self):
    super().__init__(40)

class RequestService:
  def calculateShipping(self, shipping:Shipping):
    return shipping.value

  def printInvoice(self):
    print('Printing Invoice.')

class FreeRequestService(RequestService):
  def calculateShipping(self, shipping: Shipping):
    return 'Free Resquest doesn\'t have Shipping Price'

class Payment:
  @staticmethod
  def payCredit():
    print('Pay with Credit Card.')

  @staticmethod
  def payPix():
    print('Pay with PIX.')

