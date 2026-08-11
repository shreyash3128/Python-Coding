n = int(input("Enter a number : "))
num = n
sum = 0
mul = 1
while n > 0:
    a = n % 10
    mul *= a
    sum += a
    n //= 10

if sum == mul:
    print(num, " is a spy number")
else:
    print(num, " is not a spy number")