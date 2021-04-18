#This program computes compound interest

#Prompt the user to input the inital investment
C = input('Enter the initial amount of an investment(C): ')

#Prompt the user to input the yearly rate of interest
r = input('Enter the yearly rate of interest(r): ')

#Prompt the user to input the number of years until maturation
t = input('Enter the number of years until maturation(t): ')

#Prompt the user to input the number of times the interest is compounded per year
n = input('Enter the number of times the interest is compounded per year(n): ')

def investment(C, r, n, t):
    try:
        C = float(C)
        r = float(r)
        t = float(t)
        n = float(n)
        p = round(C * (((1 + (r/n)) ** (t*n))), 2)
        print('The final value of the investment to the nearest penny is: ', p)
        return p
    except:
        print('Please, Enter a float value')
investment(C, r, n, t)