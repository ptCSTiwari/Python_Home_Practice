class employee:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def info(self):
    print(f"your name is {self.name}. and your slalary is {self.price}")

  @staticmethod  #static method call
  def sum(a, b):
    return a+b

e1 = employee("raju", 5700)
e1.info()

print(e1.sum(12, 20))