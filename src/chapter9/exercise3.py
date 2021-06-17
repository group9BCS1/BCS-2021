fname = input('Enter the file name: ')
try:
  fhand = open(fname)
except:
  print('File cannot be opened:', fname)
  exit()

lineslist=[]
emaildict={}

for line in fhand:
  lineslist = line.split()
  if line.startswith('From '):
    email=lineslist[1]
    if email not in emaildict:
      emaildict[email] = 1
    else:
      emaildict[email] += 1
print (emaildict)