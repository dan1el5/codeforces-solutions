n = int(input("Enter number of games played: "))
s = str(input())
anton = 0
danik = 0

for i in range(n):
    if s[i] == "A":
        anton+=1
    elif s[i] == "D":
        danik+=1

if anton > danik:
    print("ANTON")
elif anton < danik:
    print("DANIK")
else:
    print("Friendship")