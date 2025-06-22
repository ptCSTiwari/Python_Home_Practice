class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def first_name(self):
    l = self.name.split(" ")
    s = self.salary
    print(l,s)
    return l[0]

  def new_name(self, first):
    l = self.name.split(" ")
    new_name = f"{first} {l[1]}"
    self.name = new_name
    
e = Employee("pushp tiwari", 27000)    
print(e.first_name())
e.new_name("kaju")
print(e.name)
print(Employee.salary)