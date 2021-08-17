n = input("Enter number of stones: ")
c = input("Enter colours: ")
count = 0

for i in range(1, len(c)):
    if c[i] == c[i-1]:
        count+=1

print(count)