def open_file():
    while True:
        file_name = input("Enter input file: ")
        try:
            measles = open(file_name, "r")     #Opens the file in read mode and stores it the variable measles
            break
        except:
            print("File unable to open. Invalid name or file doesn't exist!")   #Incase the file does not exist or a wrong
            continue                                                            #name it reprompts for a write name
    return measles

def process_file(measles):
    while True:
        year = input("Enter year: ")
        if len(year) == 4:        #this ensures that the year has four characters
            break
        else:
            print("Invalid year. Year MUST be four digits")  #this makes it reprompt for a four character year
            continue
    while True:         #this loop assigns the income level 
        print("Income levels;\n Input 1 for WB_LI\n Input 2 for WB_LMI\n Input 3 for WB_UMI\n Input 4 for WB_HI")
        income = input("Enter income level(1,2,3,4): ")
        if income == "1":
            income = "WB_LI"
            break
        elif income == "2":
            income = "WB_LMI"
            break
        elif income == "3":
            income = "WB_UMI"
            break
        elif income == "4":
            income = "WB_HI"
            break
        else:
            print("Invalid income level!")    #an invalid input reprompts till the right one is made
            continue

    count = 0
    percentages = []
    countries = []
    for line in measles:
        if (line[88:92] == year) and (line[51:56] == income or line[51:57] == income): #Ensures the criteria is met
            count +=1
            percentages.append(int(line[59:61]))  #adds percentages to the list percentages
            country = line[0:51]
            country = str(country)
            country = country.strip()
            countries.append(country)        #adds percentages to the list of countries
            continue
    
    country_percentage = dict(zip(countries,percentages))    #Creates a dictionary with country as the key and percentage as values
                                                            
    if count > 0:
        percent_sum = sum(percentages)  
        percent_avg = percent_sum/count   #average of percentages
        max_percentage = max(percentages)
        min_percentage = min(percentages)
         
        #this gets countries for maximum percentages to this list 
        max_country = [country for country,percentage in country_percentage.items() if percentage == max_percentage]
        #this gets countries for minimum percentages to this list
        min_country = [country for country,percentage in country_percentage.items() if percentage == min_percentage]
 
        print(f"Nunber of countries in the record: {count}")
        print(f"Average percentage for {year} with {income} is {percent_avg:.1f}%")

        print(f"Country(ies) have maximum percentage in {year} with {income} of {max_percentage}%")  
        for i in max_country:   #prints contries with maximum percentages
            print("   >",i)
        print(f"Country(ies) have minimum percentage in {year} with {income} of {min_percentage}%")  
        for i in min_country:    #prints contries with minimum percentages
            print("   >",i)

    else:    #if there is no item in the list, it prints this
        print(f"The year {year} does not exist in the record...")

def main():
    measles = open_file()
    process_file(measles)
    measles.close()

main()     