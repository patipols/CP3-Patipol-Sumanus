def vatCal(amount):
  totalAmount = amount + (amount * (7/100))
  return totalAmount

totalAmount = float(input('Input Total Amount: '))
print(vatCal(totalAmount))  