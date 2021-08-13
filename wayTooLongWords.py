userWord = str(input("Enter a word"))

if (len(userWord)> 10):
    print(userWord[0], len(userWord)-2, userWord[-1])
else:
    print(userWord) 