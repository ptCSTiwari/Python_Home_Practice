#iska bhi advanced version hai

#this if first type we can write
# def decorator(function):
#   def wrapper():
#     print("i am going to priint hello word")
#     function()
#     print("i havae did my execution successfully")
#   return wrapper
  
# def execution():
#   print("This what i wanted to print") 

# f = decorator(execution)
# f()



#with small syntex and code
def decorator(function):
  def wrapper():
    print("i am going to priint hello word")
    function()
    print("i havae did my execution successfully")
  return wrapper

@decorator 
def execution():
  print("This what i wanted to print") 

execution()