from functools import reduce
num = [23,524,56,32,53,2,4,7,35645,2,5,2,8,3,5,6,7,8,9,10,11,12,13,14,15]
def sum(a, b):
  return a+b

c = reduce(sum, num)
print(c)