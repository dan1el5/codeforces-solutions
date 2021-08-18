s = str(input("Enter first word: "))
t = str(input("Enter second word: "))

if s[::1] == t[::-1]:
    print("YES")
else:
    print("NO")

