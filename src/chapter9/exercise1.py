fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()


words_table = []
for line in fhand:
    parts = line.split()
    for part in parts:
        words_table.append(part)

text = {}
for word in words_table:
    if word not in text:
        text[word] = 1
    else:
        text[word] = + 1

# Print out the dictionary
print(text)