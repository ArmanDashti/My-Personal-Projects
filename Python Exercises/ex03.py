list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = []
check = int(input("Enter A Number: "))
for x in list:
    if x < check:
        newList.append(x)
print(newList)