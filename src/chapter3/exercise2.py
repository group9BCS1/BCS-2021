hrs = input('Enter Hours:')
try:
  hours = float(hrs)
  rt = input('Enter Rate:')
  rate = float(rt)
  pay = hours * rate
  if hours <= 40:
    print('Pay: ', pay)
  else:
    pay_above_40 = (40* rate + (hours-40)*1.5*rate)
    print ('Pay =', pay_above_40)
except:
    print('Error, please enter numeric input')