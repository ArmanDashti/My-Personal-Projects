from stack import Stack

def is_matched(x, y):
    if x == '(' and y == ')':
        return True
    elif x == '[' and y == ']':
        return True
    elif x == '{' and y == '}':
        return True
    else:
        return False

def is_paren_balanced(paren):
    is_balanced = True
    index = 0
    s = Stack()
    for ch in paren:
        if ch in "([{":
            s.push(ch)
        else:
            if not s.is_empty():
                if is_matched(s.top(), ch):
                    s.pop()
                    index += 1
                else:
                    is_balanced = False
            else:
                is_balanced = False
    return is_balanced

