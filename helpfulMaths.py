s = input()
num1 = num2 = num3 = 0

for i in range(len(s)):
    if s[i] == '1':
        num1 += 1
    elif s[i] == '2':
        num2 += 1
    elif s[i] == '3':
        num3 += 1

orderedSum = "1+" * num1 + "2+" * num2 + "3+" * num3
print(orderedSum[:-1])
