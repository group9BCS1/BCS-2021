try:
    measles = open("measles.txt", "r")
except:
    exit("File unable to open.")

file_name = input("Enter file name: ")   
year = input("Enter year: ")

if len(year) > 4:        #this ensures entry has a maximum of four
    exit("Invalid entry of year!")

try:                         #This is for checking if entry of year is an interger or 'all/ALL'
    if year == "all" or year == "ALL" or (year == int(year)):
        pass
except:
    print("Invalid entry of year!")
    exit()

new_file = open(file_name,'w')      #incase the name file exists, this will overwrite it
for line in measles:
    if (line[88:92] == year) or (line[88:91] == year) or (line[88:90] == year) or (line[88:89] == year):
        new_file.write(line)    #add content to the file
    elif year == line[88:88] or year == "all" or year == "ALL":
        new_file.write(line)       #add content to the file

print("Process complete Check your created file.")