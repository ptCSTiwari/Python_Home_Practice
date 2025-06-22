class Employee:
  def __init__(self, name, income):
    self.name = name
    self.income = income

  def __str__(self):
     return f"name: {self.name} \n income: {self.income}"

  def __repr__(self):
    return f"name = {self.name} \n income = {self.income}"
  

e = Employee("john", 3232)
print(e.name, e.income)
# print(e.name, "\n", e.income) 
print(str(e))
print(repr(e))
