n = input("Enter number of games played: ")
s = input()
anton = 0
danik = 0

for i in s:
    if i == "A":
        anton+=1
    elif i == "D":
        danik+=1

if anton > danik:
    print("ANTON")
elif anton < danik:
    print("DANIK")
else:
    print("Friendship")