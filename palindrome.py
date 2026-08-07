print("Palindrome Logic 1")
str = input("enter a string to check palindrome : ")
str = str.casefold() # for casefold compare

if (str == str[::-1]):
    print("Palindrome String")
else:
    print("Not a Palindrome String")
print()

print("Palindrome Logic 2")
rstr = ""
for i in str:
    rstr = i + rstr
if (str == rstr):
    print("Palindrome String")
else:
    print("Not a Palindrome String")

print("Palindrome Number")
n = int(input("Enter number to check for palindrome : "))
temp = n
rev = 0
while (n>0):
    d = n % 10
    rev = rev * 10 + d
    n = n // 10
if (temp == rev):
    print("The number is palindrome.")
else:
    print("The number is not palindrome.")