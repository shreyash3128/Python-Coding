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