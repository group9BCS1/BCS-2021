fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

dictionary_addresses = dict()           # Initialize variables
lst = list()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1       # First entry
        else:
            dictionary_addresses[words[1]] += 1      # Additional counts

for key, val in list(dictionary_addresses.items()):
    lst.append((val, key))              # Fills list with value, key of dict

lst.sort(reverse=True)                  # Sorts by highest value

for key, val in lst[:1]:                # Only displays the largest value
    print(val, key)