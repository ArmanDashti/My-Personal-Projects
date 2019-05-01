from stack import Stack
def int_to_bin(int_num):
    s = Stack()
    while (int_num > 0):
        remainder = int_num % 2
        s.push(remainder)
        int_num //= 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num


print(int_to_bin(10))