def getfl(list):
    newList = []
    newList.append(list[0]) 
    newList.append(list[-1])
    return newList
list1 = [1,2,3,4,5]
print (list1)
list2 = getfl(list1)
print (list2)