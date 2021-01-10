menuList = []

def showInvoice():
  totalAmt = 0
  print('Max Food House'.center(50,'*'))
  for i in range(len(menuList)):
    print('Menu name is ',menuList[i][0], ' and price is {:.2f}'.format(menuList[i][1]),' Baht')
    totalAmt += menuList[i][1]
  print('-'*50)  
  print('Total Amount is {:.2f}'.format(totalAmt),' Baht')    

while True:
  menuName = input('Input Menu Name:')
  if menuName.lower() == 'exit':
    break
  else:
    menuPrice = float(input('Input Menu Price:'))
    menuList.append([menuName,menuPrice])
showInvoice()
     