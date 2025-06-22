from functools import reduce
a = [23, 35, 45, 4, 32, 23, 3, 2]

def square(m):
  return m*m

def greater_9(m):
  if(m>9):
    return m
  
def sum(m,n):
  c = m+n
  return c
  
new = list(map(square, a))   #we can use new= list(map(lambda x: x*x, numbers))
print(new)

greater = list(filter(greater_9, a))  #greater = list(filter(lambda x: x>9, a))
print(greater)

c = reduce(sum, a)
print(c)