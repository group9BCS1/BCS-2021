file = input("Enter a file name: ")

try:
    fhand = open(file)
except:
    print('File cannot be opened:', file)
    exit()

# Handles one line at a time
for line in fhand: 
# Removes newline and capitalizes                     
    shout = line.rstrip().upper()       
    print(shout)

