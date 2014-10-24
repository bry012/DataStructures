__author__ = 'bryan'
from DLL import DLL


class Deque(object):
    def __init__(self):
        self.DLL = DLL()

    def popEnd(self):
        return self.DLL.pop(True)

    def popBeginning(self):
        return self.DLL.pop(False)

    def append(self,data):
        self.DLL.append(data)

    def add(self,data):
        self.DLL.add(data)

    def printQueue(self):
        currentNode = self.DLL.head
        while currentNode != None:
            print(str(currentNode))
            currentNode = currentNode.next

    def length(self):
        return self.DLL.length()