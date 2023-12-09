class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.full():
            print("Stack is full")
        else:
            self.items.append(item)

    def pop(self):
        if(self.items):
            return self.items.pop()
        
        return None

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.limit == len(self.items)

    def search(self, target):
        if target in self.items:
            return (len(self.items)-1) - self.items.index(target)
        else:
            return -1
