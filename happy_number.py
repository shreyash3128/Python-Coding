num = int(input("Enter a number : "))
while sum != 1 and sum != 4:
    sum = 0
    while num > 0:
        temp = num % 10
        sum += (temp * temp)
        num //= 10
    num = sum
if sum == 1:
    print("Happy Number")
else:
    print("Unhappy number")