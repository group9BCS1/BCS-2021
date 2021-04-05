#This program prompts the user for age as an integer
#This then prints out their eligibility to vote

#This prompts the user for an age
years = input('Enter your age: ')
try:
    age = int(years)
    if age >= 18:
        print ('You can vote')
    elif age >= 0 and age <= 17:
        print ('Too young to vote')
    else:
        print('You are a time traveller')
except:
    print('Enter a numeric value')