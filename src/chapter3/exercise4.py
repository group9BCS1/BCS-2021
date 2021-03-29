age = int(input('Age: '))
if age > 17:
    print ('You can vote')
elif 0 <= age and age <= 17:
    print ('Too young to vote')
else:
    print('You are a time traveller')