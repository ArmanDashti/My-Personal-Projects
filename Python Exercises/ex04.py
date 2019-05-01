var = int(input("Enter A Number:"))
list = []
for i in range(1,var+1):
    if var%i == 0:
        list.append(i)
print(list)