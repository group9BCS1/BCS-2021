fhand = open('mbox-short.txt')
# Handles one line at a time
for line in fhand: 
# Removes newline and capitalizes                     
    shout = line.rstrip().upper()       
    print(shout)

