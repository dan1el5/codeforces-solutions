import random

numProblems = int(input("Enter number of problems: "))
total = 0

for i in range(numProblems):
    petya, vasya, tonya = random.randint(0,1), random.randint(0,1), random.randint(0,1)
    print(petya, vasya, tonya)
    if (petya + vasya + tonya >= 2):
        total+=1
    
print(total)
