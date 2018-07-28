# def fibonacci(num):
#     var1 = 1
#     var2 = 1
#     fib = [1,1]
#     for i in range(num-2):
#         var = var1+var2
#         fib.append(var)
#         var1 = var2
#         var2 = fib[-1]
#     return fib
# num = int(input("Enter a number: "))
# print(fibonacci(num))
def fibonacci():
    num = int(input("Enter a number: "))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] +  fib[i-1])
            i += 1
    return fib
result = fibonacci()
print(result)