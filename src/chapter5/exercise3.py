# This is exercise3 for Group9BCS
"""Group 9 members
1. WESONGA BOB 2020/BCS/092/PS
2. ARYAZAYO KEITH 2020/BCS/022/PS
3. MAYANJA ROBERT 2020/BCS/043/PS
4. OGENA ALLAN PAUL 2020/BCS/003
"""


# 22nd April,2021
# This is a program that will stimulate a simple change maker for a vending machine

# creating function for menu of deposit selection
def deposit_menu():
    print(
        "Menu for deposits:\n  'n' - deposit a nickel\n  'd' - deposit a dime\n  'q' - deposit a quarter\n  'o' - deposit a one dollar bill\n  'f' - deposit a five dollar bill\n  'c' - cancel the purchase\n")


def paymentDue(price):
    a = price // 1  # Gives number of dollars
    b = price % 1  # Gives number of cents
    if total_deposit_due < price and a != 0:
        print(f"Payment due: {a:.0f} dollars and {b * 100:.0f} cents")
    elif total_deposit_due < price and a == 0 and b != 0:
        print(f"Payment due: {b * 100:.0f} cents")


# main program starts here
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
    # requesting price
    price = input("Enter the purchase price (xx.xx) or `q' to quit: ")
    try:

        if price == "q":
            print("Quiting...")
            break
        price = float(price)
        priceDue = price
        if (price > 0) and (((price * 100) % 5) == 0):
            deposit_menu()
            total_deposit = 0.00
            total_deposit_due = total_deposit
            paymentDue(price)
            while price > total_deposit:
                dep = input("Indicate your deposit: ")
                if dep == 'c':
                    if total_deposit == 0:  # no refund given when amount deposited is 0
                        print("No refund.")
                        break
                    elif total_deposit > 0:
                        print("Please take your refund:\n")  # Function change
                        r_quarter = int(total_deposit // 0.25)
                        total_deposit = total_deposit % 0.25
                        r_dime = int(total_deposit // 0.1)
                        total_deposit = total_deposit % 0.1
                        r_nickle = int(total_deposit // 0.05)

                        if (r_quarter == 0) and (r_dime == 0) and (r_nickle != 0):
                            print(f"{r_nickle} nickles")
                            n = n - r_nickle
                        elif (r_quarter == 0) and (r_dime != 0) and (r_nickle == 0):
                            print(f"{r_dime} dimes")
                            d = d - r_dime
                        elif (r_quarter != 0) and (r_dime == 0) and (r_nickle == 0):
                            print(f"{r_quarter} quaters")
                            q = q - r_quarter
                        elif (r_quarter == 0) and (r_dime != 0) and (r_nickle != 0):
                            print(f"{r_dime} dimes\n{r_nickle} nickles")
                            d = d - r_dime
                            n = n - r_nickle
                        elif (r_quarter != 0) and (r_dime == 0) and (r_nickle != 0):
                            print(f"{r_quarter} quaters\n{r_nickle} nickles")
                            q = q - r_quarter
                            n = n - r_nickle
                        elif (r_quarter != 0) and (r_dime != 0) and (r_nickle == 0):
                            print(f"{r_quarter} quaters\n{r_dime} dimes")
                            q = q - r_quarter
                            d = d - r_dime
                        elif (r_quarter != 0) and (r_dime != 0) and (r_nickle != 0):
                            print(f"{r_quarter} quaters\n{r_dime} dimes\n{r_nickle} nickles")
                            q = q - r_quarter
                            d = d - r_dime
                            n = n - r_nickle

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
            if dep == "c":  # if the user had cancelled payment, this makes the program just pass back to the beginning
                print(f"Stock contains:\n {n} nickles\n {d} dimes\n {q} quaters\n {o} ones\n {f} fives ")
                pass
            elif total_deposit == price:
                print("No change.")
                print(f"Stock contains:\n {n} nickles\n {d} dimes\n {q} quaters\n {o} ones\n {f} fives ")
                continue
            elif total_deposit > price and total_deposit != price:
                print("Take your change: ")
                change = round(total_deposit - price, 2)  # Change to be dispensed

                c_quarter = int(change // 0.25)
                change = change % 0.25
                c_dime = int(change // 0.1)
                change = change % 0.1
                c_nickle = int(change // 0.05)
                if (c_quarter == 0) and (c_dime == 0) and (c_nickle != 0):
                    print(f"{c_nickle} nickles")
                    n = n - c_nickle
                elif (c_quarter == 0) and (c_dime != 0) and (c_nickle == 0):
                    print(f"{c_dime} dimes")
                    d = d - c_dime
                elif (c_quarter != 0) and (c_dime == 0) and (c_nickle == 0):
                    print(f"{c_quarter} quaters")
                    q = q - c_quarter
                elif (c_quarter == 0) and (c_dime != 0) and (c_nickle != 0):
                    print(f"{c_dime} dimes\n{c_nickle} nickles")
                    d = d - c_dime
                    n = n - c_nickle
                elif (c_quarter != 0) and (c_dime == 0) and (c_nickle != 0):
                    print(f"{c_quarter} quaters\n{c_nickle} nickles")
                    q = q - c_quarter
                    n = n - c_nickle
                elif (c_quarter != 0) and (c_dime != 0) and (c_nickle == 0):
                    print(f"{c_quarter} quaters\n{c_dime} dimes")
                    q = q - c_quarter
                    d = d - c_dime
                elif (c_quarter != 0) and (c_dime != 0) and (c_nickle != 0):
                    print(f"{c_quarter} quaters\n{c_dime} dimes\n{c_nickle} nickles")
                    q = q - c_quarter
                    d = d - c_dime
                    n = n - c_nickle

                print(f"Stock contains: \n {n} nickles\n {d} dimes\n {q} quaters\n {o} ones\n {f} fives ")
                continue
        else:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")
            continue
    except:
        print("Invalid input!")
        continue