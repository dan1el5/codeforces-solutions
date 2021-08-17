first = str(input("Enter first string: ")).lower()
second = str(input("Enter second string: ")).lower()

if first > second:
    print("1")
elif first < second:
    print("-1")
else:
    print("0")