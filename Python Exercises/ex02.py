var = int(input("Enter a number: "))
if(var%2 == 0):
    if(var%4 == 0):
        print("{} is dividable by 4".format(var))
    else:
        print("{} is an even number.".format(var))    
else:
    print("{} is an odd number.".format(var))
check = int(input("Enter another number: "))
if(var%check == 0):
    print("{} is dividable by {}".format(var,check))
else:
    print("{} isn't dividable by {}".format(var,check))