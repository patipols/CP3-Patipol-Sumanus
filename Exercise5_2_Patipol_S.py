username = input("Username :")
password = input("Password :")

if username == 'admin' and password == '1234':
  print('------Welcome to Max Shop------')
  print('------1. Coffee 10 THB-------')
  print('------2. Banana  8 THB-------')
  print('------3. Water   6 THB-------')
  selectValue = int(input("Select Product >>>"))
  
  priceCoffee = 10
  priceBanana = 8
  priceWater = 6

  demand = int(input("-----Number of Qty :"))
  
  if selectValue == 1:
    print("Number of Coffee :",demand)
    print("Total Amount: ",demand * priceCoffee)
  elif selectValue == 2:
    print("Number of Banana :",demand)
    print("Total Amount: ",demand * priceBanana)
  elif selectValue == 3:
    print("Number of Water :",demand)
    print("Total Amount: ",demand * priceWater)
  else:
    print("Not have product selected")
    
else:
  print("Username or Password incorrect!!!!")