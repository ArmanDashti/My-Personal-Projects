def get_list_with_for(list):
    for i in list:
        if list.count(list[i]) > 1:
            list.remove(list[i])
    return list

def get_list_with_set(list):
    newList = []
    list = set(list)
    newList.extend(list)
    return newList

list = [1,1,1,2,3,3,4,2,4,5,6,7,8,7,6,7,8]
newList1 = get_list_with_for(list)
print(newList1)
newList2 = get_list_with_set(list)
print(newList2)