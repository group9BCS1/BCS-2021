attendants = input('Enter the number of people attending the wedding:')
try:
  int(attendants)
  if int(attendants) >= 200:
    print('$20,000')
  elif int(attendants) >= 100 and int(attendants) <= 200:
    print('$15,000')
  elif int(attendants) >= 50 and int(attendants) <= 100:
    print('$10,000')
  elif float(attendants) > 0 and float(attendants) <= 50:
    print('$4,000')
  else:
    print('Enter an appropriate number of attendants')
except:
    print('Enter an appropriate number of attendants')