#factorial function
def fact(n):
    f = 1
    i = 1
    while i <= n:
        f *= i
        i += 1
    return f

#taking input
nLines = int(input("Enter the number of lines : "))

for j in range(nLines):
    for k in range(j+1):
        print(fact(j) // (fact(k) * fact(j - k)), " ", end = "")
    print()