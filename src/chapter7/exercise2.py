fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
confidencesum=0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:') :
      count +=1
      confidence = float(line[20:26])
      confidencesum += confidence
averageconfidence =  confidencesum/count
print ("Average spam confidence: ", str(averageconfidence))

