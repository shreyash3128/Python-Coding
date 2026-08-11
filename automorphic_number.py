n = int(input("Enter a number : "))
num = n
sq = n * n
t = 10
equal = False

print ("Square of ", n, " is", sq)

while n > 0:
    r = sq % t
    if num == r:
        equal = True
        break
    n //= 10
    t *= 10

if (equal):
    print(num, " is an automorphic number")
else:
    print(num, " is not an automorphic number")