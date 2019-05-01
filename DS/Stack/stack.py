class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)
    
    def push(self, items):
        self.items.append(items)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.items) == 0
    
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty!"