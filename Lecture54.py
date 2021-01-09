def login(username,password):
  while username != 'admin' or password != '1234':
    print('Wrong')
    username = input('Username: ')
    password = input('Password: ')

def showMenu():
  print('----------iShop------------')
  print('1. Vat Calculator')
  print('2. Price Calculator')

def selector():
  option = input('Choose Selector: ')
  return option     

def vatCal():
  print('----------1. Vat Calculator----------------')
  totalAmount = float(input('Input Total Amount: '))  
  totalAmount = totalAmount + (totalAmount * (7/100))
  print(totalAmount)

def ProdCal():
  print('-----------2. Price Calculator--------------')
  priceProduct1 = float(input('Input Price of Product 1: '))  
  priceProduct2 = float(input('Input Price of Product 2: '))  
  totalAmount = priceProduct1 + priceProduct2
  print(totalAmount) 

username = input('Username: ')
password = input('Password: ')

login(username,password)
showMenu()
option = selector()
if option == '1':
  vatCal()
elif option == '2':
  ProdCal()
else:
  print("Not Correct")