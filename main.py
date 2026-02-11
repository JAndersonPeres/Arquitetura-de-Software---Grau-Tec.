class Client:
  def __init__(self, name):
    self.name = name

  def introduce(self):
    print(f"Client: {self.name}")

client = Client("Mary")
client.introduce()
