
daysdict = {}
dayslist = []

with open("mbox-short.txt") as f:
  for line in f:
    dayslist = line.split()
    if len(dayslist) > 3 and line.startswith('From'):
      day = dayslist[2]
      if day not in daysdict:
        daysdict[day] = 1
      else:
        daysdict[day] += 1
  print (daysdict)