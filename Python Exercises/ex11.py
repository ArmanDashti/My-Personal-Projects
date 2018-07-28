def is_prime(num):
    check = True
    if num == 1:
        check = False
    elif num == 2:
        check = True
    else:
        for i in range (2,num):
            if num % i == 0:
                check = False
                break
    return check
var = int(input("Enter A Number: "))
result = is_prime(var)
if result == True:
    print("{} is a prime number.".format(var))
else:
    print("{} isn't a prime number.".format(var))