import random
num = int(input("Enter the number of random No. you want : "))
max = int(input("Enter maximum value of random number : "))
print(num, "Random No. between 0 to ", max)
for i in range(num):
    print(random.randint(0, max))