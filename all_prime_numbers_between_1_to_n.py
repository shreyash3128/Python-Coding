n = int(input("Enter a number : "))
for i in range (2, n+1):
    cn = i #current number
    count = 0
    for j in range(1, cn+1):
        if cn % j == 0:
            count += 1
    if count == 2:
        print(cn)