def gallons(meter_read1,meter_read2):
    if meter_read2 > meter_read1:
        gallon = (meter_read2 - meter_read1)/10
        print("Gallons of water used: ",gallon)
    else:
        meter_read1 = 1000000000-meter_read1
        gallon = (meter_read1 + meter_read2)/10
        print("Gallons of water used: ",gallon)
    return gallon


while True:
    code = input("Enter code: ")
    if code == "r" or code == "R":
        meter_read1 = int(input("Enter beginning meter reading: "))
        meter_read2 =  int(input("Enter ending meter reading: "))
        if (meter_read1 >= 0 and meter_read1 <= 999999999) and (meter_read2 >= 0 and meter_read2 <= 999999999):
            print("Customer code: ",code)
            print("Beginning meter reading: ",meter_read1)
            print("Ending meter reading: ",meter_read2)
            gallon = gallons(meter_read1,meter_read2)
            bill = round((5.00 + gallon*0.0005),2)
            print(f"Amount billed: ${bill:.2f}\n")
        else:
            print("Invalid meter reading")

    elif code == "c" or code == "C":
        meter_read1 = int(input("Enter beginning meter reading: "))
        meter_read2 =  int(input("Enter ending meter reading: "))
        if (meter_read1 >= 0 and meter_read1 <= 999999999) and (meter_read2 >= 0 and meter_read2 <= 999999999):
            print("Customer code: ",code)
            print("Beginning meter reading: ",meter_read1)
            print("Ending meter reading: ",meter_read2)
            gallon = gallons(meter_read1,meter_read2)
            if gallon <= 4000000.00:
                bill = round(1000.00,2)
            else:
                bill = round((1000.00 + (gallon-4000000)*0.00025),2)
            print(f"Amount billed: ${bill:.2f}\n")
        else:
            print("Invalid meter reading")

    elif code == "i" or code == "I":
        meter_read1 = int(input("Enter beginning meter reading: "))
        meter_read2 =  int(input("Enter ending meter reading: "))
        if (meter_read1 >= 0 and meter_read1 <= 999999999) and (meter_read2 >= 0 and meter_read2 <= 999999999):
            print("Customer code: ",code)
            print("Beginning meter reading: ",meter_read1)
            print("Ending meter reading: ",meter_read2)
            gallon = gallons(meter_read1,meter_read2)
            if gallon <= 4000000:
                bill = round(1000.00,2)
            elif gallon > 4000000 and gallon <= 10000000:
                bill = round(2000.00,2)
            else:
                bill = round((2000 + (gallon-10000000)*0.00025),2)
            print(f"Amount billed: ${bill:.2f}\n")
        else:
            print("Invalid meter reading")

    else:
        break