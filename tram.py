stops = int(input("Enter number of stops: "))
capacity = 0
max = 0

for i in range(stops):
    exit = int(input())
    enter = int(input())
    capacity += enter-exit
    if  max < capacity:
        max = capacity

print(max)