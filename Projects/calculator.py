while True:
  try:
    a = int(input("Enter your 1st number: "))
    b = int(input("Enter your 2nd number: "))

    print("What kind of mathematical operations you want to do. \n1. Press + for sum the numbers. \n2. Press - to do a subsraction. \n3. Press * to do a multiplication operation. Press / to do a divide operation")

    o = input("Enter which operation you want to do: ")
    match o:
      case "+":
        print(f"The result is {a+b}")
      case "-":
        print(f"The result is {a-b}")
      case "*":
        print(f"The result is {a*b}")
      case "/":
        print(f"The result is {a/b}")
      case default:
        print(f"Fool!...you are trying to do wrong operation")  
  except Exception as e:
    print("You have did everything wrong!...try again")
  
