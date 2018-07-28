import random
list1 = random.sample(range(30),10)
print (list1)
list2 = random.sample(range(30),13)
print (list2)
# newList = [i for i in list1 if i in list2]
newList = [i for i in set(list1) if i in list2]
result = [i for i in newList if newList.count(i) == 1]
print(result)