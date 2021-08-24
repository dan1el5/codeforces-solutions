n = int(input("Enter number of friends: "))
h = int(input("Enter height of fence: "))
w = 0

for i in range(n):
    a = int(input())
    if (a > h):
        w+=1

print("Minimum width of the road: " , w+n)