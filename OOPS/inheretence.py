class vehical:
  location = "japan"
  def __init__(self, name, price):
    self.name = name
    self.price = price
  def need(self):
    print("your car is aweasome")
  def details(self):
    print(f"your car is name with {self.name}. ANd you  need to pay {self.price} for it")  

class bus(vehical):
  # def __init__(self, name, price, wheels):
  #   self.name = name
  #   self.price = price
  #   self.wheels = wheels
  def need(self):
    super().need()   #super function
    print("hey i like your car")

d = bus("volvo", 25)
d.need()
print(d.location)
d.details()

    