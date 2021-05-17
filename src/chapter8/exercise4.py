fname = input("Enter file name: ")
fh = open(fname)
# list for the desired output
lst = list()
# to read every line of file romeo.txt
for line in fh:
# to eliminate the unwanted blanks and turn the line into a list of words
    word= line.rstrip().split()
# check every element in word
    for element in word:
        # if element is repeated
        if element in lst:
            continue
        else :
            lst.append(element)
# sort the list (de-indent indicates that you sort when the loop ends
lst.sort()
print(lst)