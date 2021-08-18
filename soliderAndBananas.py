k = int(input("Enter initial cost of banana: "))
n = int(input("Enter amount of money you have: "))
w = int(input("Enter amount of bananas you want: "))
sum = 0

for i in range(w+1):
    sum = sum + (i*k)

if sum <= n:
    print("0")
else:
    print(sum - n)

