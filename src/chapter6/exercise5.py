str = 'X-DSPAM-Confidence: 0.8475'
 # Finds the colon character
atpos = str.find(':')
 # Extracts portion after colon
var = str [atpos+1:]
# Converts to floating point number
var = float(var)
print('This is a floating point number %g.' % (var))

