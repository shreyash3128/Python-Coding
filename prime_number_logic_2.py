x = 2
ch = 0
n = int(input("Enter a number : "))
if n <= 1:
    ch = 1
while x <= n/2:
    if n % x == 0:
        ch = 1
        break
    else:
        x += 1
if ch == 0:
    print("prime number")
else:
    print("Not a prime number")