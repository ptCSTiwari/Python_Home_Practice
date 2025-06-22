n= int(input("enter the value of n:- "))
def fib(n):
  if(n == 0 or n == 1):
  #  print(n)
    return n

  return fib(n-2) + fib(n-1)
print("Fibonacci number at position", n, "is", fib(n))
  
# print(fib(8))

  