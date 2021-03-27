#This program prompts the user for hours and rate per hour to compute gross pay

#Prompt the user to enter the hours
hours = float(input('Enter Hours: '))

#Prompt the user to enter the rate
rate = float(input('Enter Rate: '))

#This is the mathematical formula to calcualte the gross pay
grossPay = hours * rate
#Output the grosspay
print('Gross pay = ', grossPay)