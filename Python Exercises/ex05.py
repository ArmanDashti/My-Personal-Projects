import random
list1 = random.sample(range(30),10)
print (list1)
list2 = random.sample(range(30),13)
print (list2)
newList = []
for i in list1:
    if i in list2:
        newList.append(i)
# print(newList)
result = []
for element in newList:
  if element not in result:
    result.append(element)
print(result)