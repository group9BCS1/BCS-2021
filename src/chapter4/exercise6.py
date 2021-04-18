#Prompt the user for hours
hours = input("Enter Hours: ")
#Prompt the user for the rate
rate = input("Enter Rate: ")

def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
        if hours <= 40:
            wage = hours * rate
        else:
            wage = 40 * rate + (hours - 40) * 1.5 * rate
        print('Pay: ', wage)
        return wage
    except:
        print('Please, enter a float value')
pay = computepay(hours, rate)
