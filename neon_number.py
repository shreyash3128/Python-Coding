n = int(input("Enter a number : "))
t = n*n
sum = 0
while t > 0:
    a = t % 10
    sum += a
    t //= 10

if sum == n:
    print(n, "is a neon number")
else:
    print(n, "is not a neon number")