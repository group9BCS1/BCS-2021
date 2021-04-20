sum = 0
count = 0
average = 0
while True:
  try:
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

