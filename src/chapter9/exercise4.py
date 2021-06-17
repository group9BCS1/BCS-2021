fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

lineslist = []
emaildict = {}

for line in fhand:
    lineslist = line.split()
    if line.startswith('From '):
        email = lineslist[1]
        if email not in emaildict:
            emaildict[email] = 1
        else:
            emaildict[email] += 1

largest = None
for email in emaildict:
    count = emaildict[email]
    if largest is None or count > largest :
        largest = count
        largestemail = email
print('Largest:', largestemail, largest)