n = int(input("Enter a number : "))
sum = 0
while n > 0:
    a = n % 10
    sum += a
    n //= 10

print("Sum of enterf number is ", sum)