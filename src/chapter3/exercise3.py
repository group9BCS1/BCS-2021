#This program prompts the user for a score between 0.0 and 1.0 and then outputs a grade

#This prompts the user for a score
mark = input('Enter a score between 0.0 and 1.0: ')
try:
  score = float(mark)
  if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
      print('A')
    elif score >= 0.8:
      print('B')
    elif score >= 0.7:
      print('C')
    elif score >= 0.6:
      print('D')
    else:
      print('F')
  else:
    print('Bad score')
except:
    print('Bad score')