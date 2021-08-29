n = int(input("Enter number of rooms: "))
count = 0

for i in range(n):
    p = int(input("Number of people already in room: "))
    q = int(input("Room capacity: "))
    if (p<q):
        count+=1

print(count)
