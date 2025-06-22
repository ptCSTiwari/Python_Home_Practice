def divide(n , m):
  try:
    c = n/m
    print(c)
    return c
  
  except Exception as e:
    print(e)
    return None
  finally:
    print("this is always be executed")

a = int(input("numer 1: "))  
b = int(input("numer 2: "))
divide(a, b)