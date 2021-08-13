numOfStatements = int(input("Enter the number of statements:"))

i = 0
count = 0
while i < numOfStatements:
    statement = input("Enter statement: ")
    if statement == "X++":
        count+=1
        i+=1
    elif statement == "X--":
        count-=1
        i+=1

print(count)
