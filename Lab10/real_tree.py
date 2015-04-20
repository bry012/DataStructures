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

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def node_levels(self, root):
       if root == None:
           return 0
       return max(self.node_levels(root.getLeftChild()), self.node_levels(root.getRightChild())) + 1

    def height(self, root):
        return self.node_levels(root) - 1

    def print_tree(self, level=0):
        print("\t" * level + str(self.key))
        if self.leftChild:
            print("\t" * level + "[Left Child]")
            level += 1
            self.leftChild.print_tree(level)
        if self.rightChild:
            print("\t" * (level - 1) + "[Right Child]")
            self.rightChild.print_tree(level)

    def leaves(self,root):
        if not self.leftChild and not self.rightChild:
            print("Tree Leaf: %s" % self.getRootVal())
        if not root:
            return None
        if self.leftChild:
            self.leftChild.leaves(self.leftChild)
        if self.rightChild:
            self.rightChild.leaves(self.rightChild)

    def stats(self, root):
        print( "Height: %d\nRoot: %s\n" % (self.height(root),self.getRootVal()))
        print("Preoder Traversal:\n")
        self.print_tree()
        print("Leaf Nodes:\n")
        self.leaves(root)

count = 0
binary_tree = BinaryTree("Body")
binary_tree.insertLeft("Engine")
engine = binary_tree.getLeftChild()
engine.insertLeft("Front Axle")
front_axle = engine.getLeftChild()
engine.insertRight("Back Axle")
back_axle = engine.getRightChild()
front_axle.insertRight("Front Right Wheel")
front_right = front_axle.getRightChild()
front_axle.insertLeft("Front Left Wheel")
front_left = front_axle.getLeftChild()
back_axle.insertRight("Back Right Wheel")
back_right = back_axle.getRightChild()
back_axle.insertLeft("Back Left Wheel")
back_left = back_axle.getLeftChild()
front_right.insertLeft("Front Right Hub Cap")
front_left.insertLeft("Front Left Hub Cap")
back_right.insertLeft("Back Right Hub Cap")
back_left.insertLeft("Back Left Hub Cap")

binary_tree.stats(binary_tree)
