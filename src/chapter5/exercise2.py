#This program prompts the user for numbers and prints the maximum and minimum of
#the numbers
count = 0
numbers = []
while True:
    # prompts the user for a number
    line = input("Enter a number: ")
    try:
        line = int(line)
        numbers.append(line)
        count = count + 1
        maximum = max(numbers)
        minimum = min(numbers)
    except:
        if line == "done":
            break
        else:
            print("Invalid input")
# prints value of average, maximum, and minimum variable
print('Maximum =', maximum)
print('Minimum =', minimum)

