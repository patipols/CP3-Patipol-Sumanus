def showBill():
  priceTotal = 0
  print('my Food'.center(20,'-'))
  for i in range(len(menuList)):
    print(menuList[i],priceList[i])
    priceTotal += int(priceList[i])
  print('Total Amount is {:.2f}'.format(priceTotal))

menuList = []
priceList = []

while True:
  menuName = input('Input Menu name  : ')
  if menuName.lower() == 'exit':
    break
  else:
    menuPrice = input('Input Menu Price: ')
    menuList.append(menuName)
    priceList.append(menuPrice)
showBill()     