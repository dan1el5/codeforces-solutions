import random

n = int(input("Enter number of contestants: "))
k = int(input("Enter minimum score to qualify for the next round: "))
qualified = 0

for i in range(n):
    scores = random.randint(0,100)
    print(scores, end=' ')
    if scores >= k:
        qualified+=1

print('\n', qualified, "people have qualified for the next round")
