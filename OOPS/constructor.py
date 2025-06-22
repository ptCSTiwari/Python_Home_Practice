class car:
  model = "shift"
  def __init__(self, name, price, model):
    self.name = name
    self.price = price
    self.model = model

  def get_info(self):
    print(f"the name of car is {self.name}. the price of it is {self.price}. the mdel is the {self.model}")

c1 = car("tata", 25000, "lsv")
print(c1.model)
print(car.model)
c1.get_info()
# print(dir(c1))