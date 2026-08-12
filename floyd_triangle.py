n = int(input("Enter a number : "))
count = 1
for i in range(1, n+1):
    for j in range (1, i+1):
        print("{:2d}".format(count), end=" ")
        count += 1
    print()