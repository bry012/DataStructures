__author__ = 'bryan'
from Node import Node


class DLL(object):
    def __init__(self):
        self.head = Node(None, None, None)
        self.end = Node(None, None, None)

    def insert(self, nodeValue, data):

        node = self.search(nodeValue)
        if not node.previous:
            self.head = Node(data, None, self.head)

        elif node:
            node.next = Node(data,node,node.next)

    def remove(self,nodeValue):
        node = self.search(nodeValue)
        if node.previous == None:
            self.head = node.next
        elif node:
            node.previous.next = node.next

    def add(self, data):
        newNode = Node(data, None, None)
        if self.isEmpty():
            self.head = newNode
            self.end = newNode
        else:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode

    def append(self, data):
        newNode = Node(data,None,None)
        if self.isEmpty():
            self.head = newNode
            self.end = newNode
        else:
            newNode.previous = self.end
            self.end.next = newNode
            self.end = newNode

    def pop(self, isEnd):
        if isEnd:
            node = self.end
            if self.length() > 2:
                self.end.previous.next = None
            self.end = self.end.previous
            return node.data
        else:
            node = self.head
            if self.length() > 2:
                self.head.next.previous = None
            self.head = self.head.next
            return node.data

    def isEmpty(self):
        if not self.head.data:
            return True
        else:
            return False

    def length(self):
        count = 0
        currentNode = self.head
        while currentNode:
            count += 1
            currentNode = currentNode.next
        return count

    def search(self, data):
        currentNode = self.head
        while currentNode != None:
            if data == currentNode.data:
                return currentNode
            currentNode = currentNode.next
        return None




