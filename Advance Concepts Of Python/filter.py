# def number_greater_20(num):
#   if num > 20:
#     return num
#   else:
#     return None

a = [23,524,56,32,53,2,4,7,35645,2,5,2,8,3,5,6,7,8,9,10,11,12,13,14,15]

# new = list(filter(number_greater_20, a))
# print(new)

#using lambda function
new = list(map(lambda num: num**2, a))  #map function
print(new)                              #will print sqaure using map and labda function
new = list(filter(lambda num: num > 20, a))
print(new)


