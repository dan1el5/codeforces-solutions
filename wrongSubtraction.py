n = int(input("Enter a number: "))
s = int(input("Enter the number of times to subtract 1: "))

for i in range(s):
    if n%10 == 0:
        n/=10
    else:
        n-=1

print(n)
