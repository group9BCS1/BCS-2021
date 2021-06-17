fname = input('Enter the file name: ')
try:
  fhand = open(fname)
except:
  print('File cannot be opened:', fname)
  exit()

daysdict = {}
dayslist = []

for line in fhand:
  dayslist = line.split()
  if len(dayslist) > 3 and line.startswith('From'):
    day = dayslist[2]
    if day not in daysdict:
      daysdict[day] = 1
    else:
      daysdict[day] += 1
print (daysdict)