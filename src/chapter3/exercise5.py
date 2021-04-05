#This program prompts the user for the number of people attending their wedding
#It then prints the corresponding price

#This prompts the user to enter the number of attendants
attendants = input('Enter the number of people attending the wedding:')
try:
  int(attendants)
  if attendants >= 200:
    print('$20,000')
  elif attendants > 100 and attendants <= 200:
    print('$15,000')
  elif attendants > 50 and attendants <= 100:
    print('$10,000')
  elif attendants > 0 and attendants <= 50:
    print('$4,000')
  else:
    print('Enter an appropriate number of attendants')
except:
    print('Enter an integer')