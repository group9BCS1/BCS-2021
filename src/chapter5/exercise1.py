#This program prompts the user for numbers and prints
# out the total, count,and average of the numbers
sum = 0
count = 0
average = 0
while True:
  try:
    #prompts the user for a number
    x = input("Enter a number: ")
    if x == "done":
     break
    value = int(x)
    sum = value + sum
    count = count + 1
    average = sum / count
  except:
    print("Invalid input")
print(sum, count, average)

