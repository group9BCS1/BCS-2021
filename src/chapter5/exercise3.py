# creating function for menu of deposit selection
def deposit_menu():
    print("""
Menu for deposits:
'n' - deposit a nickel
'd' - deposit a dime
'q' - deposit a quarter
'o' - deposit a one dollar bill
'f' - deposit a five dollar bill
'c' - cancel the purchase
    """)

def paymentDue(price):
    a = price // 1      # Gives number of dollars
    b = price % 1       # Gives number of cents
    print(f"Payment due: {a:.0f} dollars and {b*100:.0f} cents")


#main program starts here
n = 25
d = 25
q = 25
o = 0
f = 0

print(f"""Welcome to the vending machine change maker program
Change maker initialized.
Stock contains:
   {n} nickles
   {d} dimes
   {q} quaters
   {o} ones
   {f} fives
""")

while True:
    try:
        #requesting price
        price = input("Enter the purchase price (xx.xx) or `q' to quit: ")
        if price == "q":
            print("Quiting...")
            break
        price = float(price)
        priceDue = price
        if (price > 0) and (((price*100) % 5) == 0):
            deposit_menu()
            paymentDue(price)
            total_deposit = 0.00
            while price > total_deposit:
                dep = input("Indicate your deposit: ")
                if dep == 'c':
                    print("Please take the change below",total_deposit)  # Function change

                    break
                elif dep == 'n':
                    priceDue = priceDue - 0.05
                    total_deposit = total_deposit + 0.05
                    n = n + 1
                    paymentDue(priceDue)
                    continue
                elif dep == 'd':
                    priceDue = priceDue - 0.1
                    total_deposit = total_deposit + 0.1
                    d = d + 1
                    paymentDue(priceDue)
                    continue
                elif dep == 'q':
                    priceDue = priceDue - 0.25
                    total_deposit = total_deposit + 0.25
                    q = q + 1
                    paymentDue(priceDue)
                    continue
                elif dep == 'o':
                    priceDue = priceDue - 1.0
                    total_deposit = total_deposit + 1
                    o = o + 1
                    paymentDue(priceDue)
                    continue
                elif dep == 'f':
                    priceDue = priceDue - 5.0
                    total_deposit = total_deposit + 5
                    f = f + 1
                    paymentDue(priceDue)
                    continue
                else:
                    print("Illegal selection:", dep)
                    paymentDue(price)
                    continue
            if total_deposit == price:
                print("No chnge.")
                print(f"Stock contains:\n {n} nickles\n {d} dimes\n {q} quaters\n {o} ones\n {f} fives ")
            else:
                print("Take your change:\n ")
                print(f"Stock contains: \n {n} nickles\n {d} dimes\n {q} quaters\n {o} ones\n {f} fives ")   
        else:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")
    except:
        print("Invalid input!")
        continue
