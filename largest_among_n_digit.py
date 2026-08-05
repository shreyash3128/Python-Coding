arr = []
num = int(input("Enter N number : "))
for i in range (num):
    numbers = int(input("Enter number : "))
    arr.append(numbers)
print("Largest element int he list is : ", max(arr))
print("Smallest element int he list is : ", min(arr))