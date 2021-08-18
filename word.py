s = str(input("Enter a word: "))
count = 0

for i in s:
    if i.isupper():
        count+=1

if count > len(s) / 2:
    print(s.upper())
else:
    print(s.lower())