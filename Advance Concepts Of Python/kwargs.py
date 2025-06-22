def marks(**kwargs):
  for item in kwargs.keys():
    print(f"The marks of {item} is {kwargs[item]}")

marks(tiwari=99, rajawat=32, sharma=89)