__author__ = 'bryan'


class Node(object):
    def __init__(self, data, previousNode, nextNode):
        self.data = data
        self.previous = previousNode
        self.next = nextNode

    def __str__(self):
        return self.data