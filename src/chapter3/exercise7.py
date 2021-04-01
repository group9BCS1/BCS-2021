location = str(input('Enter the location: '))
pay = float(input('Enter the pay: '))
if pay > 4000000 and location == 'Mbarara':
 	print('Sure, I can work with this')
elif location == 'Kampala':
    if pay < 10000000:
        print('No way!')
    else:
        print('Without a doubt, I’ll take it')
elif pay > 6000000:
    print('Sure, I can work with this')
elif location == 'Space':
    print('Without a doubt, I’ll take it')
else:
    print('No Thanks, I can find something better')




