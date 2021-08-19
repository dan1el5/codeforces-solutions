y = int(input("Enter year: "))

for i in range(y):
    y+=1
    thousands = y // 1000
    hundreds = (y % 1000) // 100
    tens = (y % 100) // 10
    ones = (y % 10)
    if ((thousands!=hundreds) & (thousands!=tens) & (thousands!=ones) & (hundreds!=tens) & (hundreds!=ones) & (tens!=ones)):
        break

print(y)