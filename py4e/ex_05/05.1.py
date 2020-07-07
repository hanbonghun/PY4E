largest = None
smallest = None
while True:
    num = input("Enter the number")
    if num == "done" :
        break
    try:
        n = float(num)
    except:
        print("Invalid input")
        continue
    if largest == None :
        largest = num
        smallest = num

    elif n > int(largest):
        largest = num

    elif n<int(smallest) :
    	smallest=num

print("Maximum is", largest)
print("Minimum is", smallest)
