print('Enter the two points (x1, y1) and (x2, y2): ')
x1 = int(input("Enter x1 : "))

y1 = int(input("Enter y1 : "))

x2 = int(input("Enter x2 : "))

y2 = int(input("Enter y2 : "))

result = ((((x2 - x1 )**2) + ((y2-y1)**2))**0.5)

print("The distance between", (x1, y1), "and", (x2, y2), "is : ", result)