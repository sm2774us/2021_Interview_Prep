# Don't modify __eq__() and other relational methods, because method delete() in BinarySearchTree class might mind this!
# It uses != to see if the two objects are the same object, not if they just have the same key.

class Node(object):

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.size = 1

    def setKey(self, key):
        self.key = key

    def setParent(self, node):
        self.parent = node

    def setLeftChild(self, node):
        self.left = node

    def setRightChild(self, node):
        self.right = node

    def setSize(self, size):
        self.size = size

    def incrementSize(self):
        self.size += 1

    def decrementSize(self):
        self.size -= 1

    def recomputeSize(self):
        left, right = self.left, self.right
        if left:
            leftSize = left.getSize()
        else:
            leftSize = 0
        if right:
            rightSize = right.getSize()
        else:
            rightSize = 0
        self.size = leftSize + rightSize + 1

    def getKey(self):
        return self.key
    
    def getParent(self):
        return self.parent
    
    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def getSize(self):
        return self.size

    def printNode(self):
        print("Key: {}, Parent: {}, Left child: {}, Right child: {}, Size: {}".format(self.key, self.parent, self.left, self.right, self.size))

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        """This can be used as:
           print(repr(tree.find(key, root)))
           But, it's also very useful for debugging, because debugger will show us the key of the node without the need for expanding the node.
           Of course, we can add some other pieces of information, too.
           We can return "str(self.key)" and concatenate other string to it, or we can use the form below. Anyhow, we must return a string.
        """
        return "Key: {}, Size: {}".format(self.key, self.size)
