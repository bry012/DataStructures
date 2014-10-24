__author__ = 'bryan'
__author__ = 'bryan'
# Python implementation of a Stack
# End of the list will hold the top element of the stack - think about why?
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size (self):
        return len(self.items)