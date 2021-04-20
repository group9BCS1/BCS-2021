count = 0
numbers = []
while True:
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

