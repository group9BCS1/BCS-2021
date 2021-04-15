#Prompt the user for hours
hours = float(input("Enter Hours: "))
#Prompt the user for the rate
rate = float(input("Enter Rate: "))

def computepay(hours, rate):
    if hours <= 40:
        wage = hours * rate
    else:
        wage = 40 * rate + (hours - 40) * 1.5 * rate
    return wage
pay = computepay(hours, rate)
print('Pay: ', pay)