#This program lets a user input an amount of money that they need to make change for, and dispenses the correct amount of change

#Prompt the user to enter the change
change = float(input('Enter an amount to make a change for: '))
print('Your change is... ')

print(int(change//20), 'twenties')
change = change % 20
print(int(change//10), 'tens')
change = change % 10
print(int(change//5), 'fives')
change = change % 5
print(int(change//1), 'ones')
change = change % 1
print(int(change//0.25), 'quarters')
change = change % 0.25
print(int(change//0.1), 'dimes')
change = change % 0.1
print(int(change//0.05), 'nickels')
change = change % 0.05
print(int(change//0.01), 'pennies')










