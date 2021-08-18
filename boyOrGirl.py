user = str(input("Enter username: "))

user = dict.fromkeys(user)
if len(user) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")