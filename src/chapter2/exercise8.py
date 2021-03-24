
C = int(input("Enter the initial amount of an investment(C): "))

r = float(input("Enter the yearly rate of interest(r): "))

t = int(input("Enter the number of years until maturation(t): "))

n = int(input("Enter the number of times the interest is compounded per year(n): "))

p = str(round(C * (((1 + (r/n)) ** (t*n))), 2))

print("The final value of the investment to the nearest penny is: ", p)