#Prompt the user to enter the hours
hours = input('Enter Hours: ')
try:
    float(hours)
    # Prompt the user to enter the rate
    rate = input('Enter Rate: ')
    float(rate)
    pay = hours * rate
    print('Pay:', pay)
except:
    print('Error, please enter numeric input')