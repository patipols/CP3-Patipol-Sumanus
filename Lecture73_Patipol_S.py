menuList = []
masterPrice = {'ข้าวหมกไก่':45,'ข้าวมันไก่':40,'ข้าวมันไก่ผสม':50,'ข้าวมันไก่พิเศษ':45}
def showInvoice():
  totalAmt = 0
  print('Max Food House'.center(50,'*'))
  for i in range(len(menuList)):
    print('เมนูที่',i,'คือ',menuList[i][0], ' ราคา {:.2f}'.format(menuList[i][1]),' บาท')
    totalAmt += menuList[i][1]
  print('-'*50)  
  print('ยอดรวมทั้งสิ้น {:.2f}'.format(totalAmt),' บาท')    

while True:
  menuName = str(input('ชื่อเมนู:'))
  if menuName.lower() == 'exit':
    break
  else:
    if (menuName in masterPrice) == True:
      menuList.append([menuName,masterPrice[menuName]])
    else:
      print('เมนู ',menuName,' ไม่พบราคา!!!! โปรดอัพเดทราคาของเมนูนี้')
      menuPrice = float(input('ราคา:'))
      menuList.append([menuName,menuPrice])
showInvoice()