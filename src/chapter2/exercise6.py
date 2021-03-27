#This program reads two points from the user, computes and prints the distance between the two points

#Prompt the user to enter the two coordinates
print('Enter the two points (x1, y1) and (x2, y2): ')
x1 = int(input('Enter x1 : '))

y1 = int(input('Enter y1 : '))

x2 = int(input('Enter x2 : '))

y2 = int(input('Enter y2 : '))

result = ((((x2 - x1 )**2) + ((y2-y1)**2))**0.5)

#Print out the distance
print('The distance between', (x1, y1), 'and', (x2, y2), 'is : ', result)