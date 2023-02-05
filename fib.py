import decimal

print('Enter a term. This program will find the fibonacci sequence number corresponding to it. \n')
print('Credit to math.hmc.edu for the formula. \n')

try : 
  n = decimal.Decimal(input('Enter Number:' )) 
  sqrtf = decimal.Decimal(5).sqrt() # from stackoverflow

  g = (1 + sqrtf) / 2 
  nrog = (1 - sqrtf) / 2 # negative reciprocal 

  gn = g**n
  nrogn = nrog**n

  ft = (gn - nrogn) / sqrtf   
  tf = f'{ft:.25f}' # from stackoverflow

  print('Your number is: \n' + tf)

except : 
  print('Please enter a number.')

