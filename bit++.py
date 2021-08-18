numOfStatements = int(input("Enter the number of statements:"))
count = 0

for i in range(0, numOfStatements, 1):
    statement = input("Enter statement: ")
    if statement == "X++":
        count+=1
    elif statement == "X--":
        count-=1

print(count)
