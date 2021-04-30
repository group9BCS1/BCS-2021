#This is the midterm for group9BCS1
#This program computes and displays information for a utility company which supplies water to its
# customers. For a specified customer, the program will compute and display the amount of money which
#the customer will be billed for water usage during the current billing period

def gallons(meter_read1,meter_read2):    #this function is for getting the number of gallons is water used
    if meter_read2 > meter_read1:
        gallon = (meter_read2 - meter_read1)/10
        print("Gallons of water used: ",gallon)
    else:
        meter_read1 = 1000000000-meter_read1    
        gallon = (meter_read1 + meter_read2)/10
        print("Gallons of water used: ",gallon)
    return gallon


#the program starts here
while True:
    code = input("Enter customer code: ")       #user code is fed
    if code == "r" or code == "R":
        meter_read1 = int(input("Enter beginning meter reading: "))
        meter_read2 =  int(input("Enter ending meter reading: "))
        if (meter_read1 >= 0 and meter_read1 <= 999999999) and (meter_read2 >= 0 and meter_read2 <= 999999999):
            print("Customer code: ",code)
            print(f"Beginning meter reading: {meter_read1:09d} ")
            print(f"Ending meter reading: {meter_read2:09d} ")
            gallon = gallons(meter_read1,meter_read2)
            bill = 5.00 + gallon*0.0005
            print(f"Amount billed: ${bill:.2f}\n")
        else:
            print("Invalid meter reading\n")  #incase the number is less than 0 or greater then 999999999, it is an invalid input. hence trapped

    elif code == "c" or code == "C":
        meter_read1 = int(input("Enter beginning meter reading: "))
        meter_read2 =  int(input("Enter ending meter reading: "))
        if (meter_read1 >= 0 and meter_read1 <= 999999999) and (meter_read2 >= 0 and meter_read2 <= 999999999):
            print("Customer code: ",code)
            print(f"Beginning meter reading: {meter_read1:09d} ")
            print(f"Ending meter reading: {meter_read2:09d} ")
            gallon = gallons(meter_read1,meter_read2)
            if gallon <= 4000000.00:
                bill = 1000.00
            else:
                bill = round((1000.00 + (gallon-4000000)*0.00025),2)
            print(f"Amount billed: ${bill:.2f}\n")
        else:
            print("Invalid meter reading\n")  #incase the number is less than 0 or greater then 999999999, it is an invalid input. hence trapped

    elif code == "i" or code == "I":
        meter_read1 = int(input("Enter beginning meter reading: "))
        meter_read2 =  int(input("Enter ending meter reading: "))
        if (meter_read1 >= 0 and meter_read1 <= 999999999) and (meter_read2 >= 0 and meter_read2 <= 999999999):
            print("Customer code: ",code)
            print(f"Beginning meter reading: {meter_read1:09d} ")
            print(f"Ending meter reading: {meter_read2:09d} ")
            gallon = gallons(meter_read1,meter_read2)
            if gallon <= 4000000:
                bill = round(1000.00,2)
            elif gallon > 4000000 and gallon <= 10000000:
                bill = round(2000.00,2)
            else:
                bill = round((2000 + (gallon-10000000)*0.00025),2)
            print(f"Amount billed: ${bill:.2f}\n")
        else:
            print("Invalid meter reading\n") #incase the number is less than 0 or greater then 999999999, it is an invalid input. hence trapped

    else:
        break