largest = 0
smallest = 0
num = input("Enter a number: ")
smallest = int(num)
while True:
    if num == "done" : break
    try :
        n = int(num)
        if n > largest :
            largest = n
        if n < smallest :
            smallest = n
    except :
        n = -1
        print("Invalid input")
    num = input("Enter a number: ")
print("Maximum is", largest)
print("Minimum is", smallest)