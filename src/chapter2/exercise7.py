#This program lets a user input an amount of money that they need to make change for, and dispenses the correct amount of change

#Prompt the user to enter the change
amt = float(input('Enter an amount to make a change for: '))
print('Your change is... ')

print(int(amt//20), 'twenties')
amt = amt % 20
print(int(amt//10), 'tens')
amt = amt % 10
print(int(amt//5), 'fives')
amt = amt % 5
print(int(amt//1), 'ones')
amt = amt % 1
print(int(amt//0.25), 'quarters')
amt = amt % 0.25
print(int(amt//0.1), 'dimes')
amt = amt % 0.1
print(int(amt//0.05), 'nickels')
amt = amt % 0.05
print(round(amt//0.01), 'pennies')
amt = amt % 0.01








