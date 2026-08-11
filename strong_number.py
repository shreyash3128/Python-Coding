num = int(input("Enter the number : "))
save_num = num
sum = 0
while num > 0:
    a = num % 10
    b = 1
    for i in range(1, a+1):
        b *= i
    sum += b
    num //= 10

if save_num == sum:
    print(save_num, "is a strong number")
else:
    print(save_num, "is not a strong number")