fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

dictionary_hours = dict()               # Initialize variables
lst = list()

for line in fhand:
    words = line.split()
    if len(words) < 5 or words[0] != 'From':
        continue

    col_pos = words[5].find(':')
    hour = words[5][:col_pos]
    if hour not in dictionary_hours:
        dictionary_hours[hour] = 1      # First entry
    else:
        dictionary_hours[hour] += 1     # Additional counts

for key, val in list(dictionary_hours.items()):
    lst.append((key, val))              # Fills list with hour, count of dict

lst.sort()                              # Sorts by hour

for key, val in lst:
    print(key, val)