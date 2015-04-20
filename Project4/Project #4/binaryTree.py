class BinaryTree:
    # Constructor: Accepts object to be the root
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    # Inserts a left node
    def insertLeft(self,newNode):
        # If the left child is None
        if self.leftChild == None:
            # Create a new binary tree with the new node
            # and set it as the left child
            self.leftChild = BinaryTree(newNode)
        else:
            # Create a new binary tree with the new node
            t = BinaryTree(newNode)
            # Set the left child of the new tree to be the
            # current left child
            t.leftChild = self.leftChild
            # Set new tree to be left child
            self.leftChild = t

    # Inserts a right node
    def insertRight(self,newNode):
        # If the right child is None
        if self.rightChild == None:
            # Create a new binary tree with the new node
            # and set it as the right child
            self.rightChild = BinaryTree(newNode)
        else:
            # Create a new binary tree with the new node
            t = BinaryTree(newNode)
            # Set the left child of the new tree to be the
            # current left child
            t.rightChild = self.rightChild
            # Set new tree to be left child
            self.rightChild = t

    # Return the right child
    def getRightChild(self):
        return self.rightChild

    # Return the left child
    def getLeftChild(self):
        return self.leftChild

    # Set the root value
    def setRootVal(self,obj):
        self.key = obj

    # Get the root value
    def getRootVal(self):
        return self.key
        
    def postorder(self):        
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)
    
