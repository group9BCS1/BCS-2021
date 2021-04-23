total = 0
count = 0
avg = 0

while True:
    x = input('Enter a number: ')
    try:
        x = int(x)
        total = total + x
        count = count + 1
        avg = total/count      
    except:
        if x == 'done':                     #when user types done, total, number of values entered and average is printed
            print(total, count, avg)
            break
        else:
            print('Invalid input')