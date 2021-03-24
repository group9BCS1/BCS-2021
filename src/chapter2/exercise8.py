#This program computes compound interest

#Prompt the user to input the inital investment
C = int(input('Enter the initial amount of an investment(C): '))

#Prompt the user to input the yearly rate of interest
r = float(input('Enter the yearly rate of interest(r): '))

#Prompt the user to input the number of years until maturation
t = int(input('Enter the number of years until maturation(t): '))

#Prompt the user to input the number of times the interest is compounded per year
n = int(input('Enter the number of times the interest is compounded per year(n): '))

#This is the formula to compute the compound interest. It is printed to the nearest penny
p = str(round(C * (((1 + (r/n)) ** (t*n))), 2))

#This outputs the compound interest to the nearest penny
print('The final value of the investment to the nearest penny is: ', p)