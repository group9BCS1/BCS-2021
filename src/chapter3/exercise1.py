#Prompt the user to enter the hours
hours = float(input('Enter Hours: '))

#Prompt the user to enter the rate
rate = float(input('Enter Rate: '))

if hours <= 40:
 	print('Pay:', hours  * rate)
elif hours > 40:
	print('Pay:', 40* rate + (hours-40)*1.5*rate)




