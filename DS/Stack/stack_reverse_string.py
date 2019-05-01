from stack import Stack

def reverse_string(input_str):
    stack = Stack()
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

input_str = "Hello"
stackx = Stack()
stackx.push("a")
stackx.push("b")
stackx.push("c")
stackx.push("d")
stackx.push("e")
print (reverse_string(input_str))    