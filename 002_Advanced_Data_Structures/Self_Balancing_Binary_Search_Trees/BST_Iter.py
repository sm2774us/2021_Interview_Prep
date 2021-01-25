"""
Iterative version

Contains methods for tree traversal.
This version assumes that keys of all nodes in a tree are different, that they don't repeat.
"""

from Node import Node
from collections import deque


class BinarySearchTree(object):

    def __init__(self, root):
        """Expects a root node object as input."""
        self.root = root

    def __str__(self):
        return "Root = {}".format(repr(self.root))

    def __repr__(self):
        """Useful for debugging.
        The first part returns the original value of __repr__(), which contains type of the object and its address in memory.
        The second part gives us information about the root of the tree, which is its key, because it calls its __repr__() method.
        """
        return super(BinarySearchTree, self).__repr__() + " Root = {}".format(repr(self.root))

    def getRoot(self):
        return self.root

    def inOrder(self):
        """Returns the whole tree (nodes' keys) in in-order traversal, as a list. Has no input parameters. Works iteratively."""
        current = self.root
        if not current:
            return []
        self.result = []
        stack = []                                              # stack contains nodes
        while True:
            while current:
                stack.append(current)
                current = current.getLeftChild()
            if stack:
                current = stack.pop()
                self.result.append(current.getKey())            # visit()
                current = current.getRightChild()
            else:
                return self.result

    def preOrder(self):
        """Returns the whole tree (nodes' keys) in pre-order traversal, as a list. Has no input parameters. Works iteratively."""
        root = self.root
        self.result = []
        stack = [root]                                          # stack contains nodes
        while stack:
            current = stack.pop()
            self.result.append(current.getKey())                # visit()
            if current.getRightChild():
                stack.append(current.getRightChild())
            if current.getLeftChild():
                stack.append(current.getLeftChild())
        return self.result

    def postOrder(self):
        """Returns the whole tree (nodes' keys) in post-order traversal, as a list. Has no input parameters. Works iteratively."""
        self.result = []
        stack = []                                              # stack contains nodes
        boolStack = []                                          # For each element on the node stack, a corresponding value is stored on the bool stack. If this value is true, then we need to pop and visit the node on next encounter.
        current = self.root
        while current:
            stack.append(current)
            boolStack.append(False)
            current = current.getLeftChild()
        while stack:
            current = stack[-1]
            alreadyEncountered = boolStack[-1]
            if alreadyEncountered:
                self.result.append(current.getKey())            # visit()
                stack.pop()
                boolStack.pop()
            else:
                boolStack.pop()
                boolStack.append(True)
                current = current.getRightChild()
                while current:
                    stack.append(current)
                    boolStack.append(False)
                    current = current.getLeftChild()
        return self.result

    def BFS(self):
        """Returns the whole tree (nodes' keys) in level-order traversal, as a list. Has no input parameters. Works iteratively."""
        root = self.root
        self.result = []
        queue = deque([root])                                   # queue contains nodes
        while queue:
            current = queue.popleft()
            self.result.append(current.getKey())                # visit()
            if current.getLeftChild():
                queue.append(current.getLeftChild())
            if current.getRightChild():
                queue.append(current.getRightChild())
        return self.result

    def find(self, key):
        """Inputs: key is a numerical value.
           Returns a node object - if the key (value) is found exactly, than it returns that node, otherwise it returns the node under which the searched key should be.
        """
        # Only in the first iteration will the root be the root node object; in subsequent iterations it will actually be a node object, but not the root anymore.
        root = self.root
        while root:
            if root.getKey() == key:
                return root
            elif root.getKey() > key:
                if root.getLeftChild():
                    root = root.getLeftChild()
                    continue
                return root
            else:                                               # root.getKey() < key:
                if root.getRightChild():
                    root = root.getRightChild()
                    continue
                return root

    def next(self, node):
        """Input is a node object.
           Outputs the next node object in terms of key value, or None, if we input the largest one.
        """
        if node.getRightChild():
            return self.leftDescendant(node.getRightChild())
        else:
            return self.rightAncestor(node)

    def leftDescendant(self, node):
        if not node.getLeftChild():
            return node
        else:
            return self.leftDescendant(node.getLeftChild())

    def rightAncestor(self, node):
        if node.getParent():
            if node.getKey() < node.getParent().getKey():
                return node.getParent()
            else:
                return self.rightAncestor(node.getParent())
        else:
            return None

    def previous(self, node):
        """Input is a node object.
           Outputs the previous node object in terms of key value, or None, if we input the smallest one.
        """
        if node.getLeftChild():
            return self.rightDescendant(node.getLeftChild())
        else:
            return self.leftAncestor(node)

    def rightDescendant(self, node):
        if not node.getRightChild():
            return node
        else:
            return self.rightDescendant(node.getRightChild())

    def leftAncestor(self, node):
        if node.getParent():
            if node.getKey() > node.getParent().getKey():
                return node.getParent()
            else:
                return self.leftAncestor(node.getParent())
        else:
            return None

    def rangeSearch(self, x, y):
        """Inputs: numbers x, y
           Output: A list of nodes with key between x and y
        """
        L = []
        node = self.find(x)
        while node and node.getKey() <= y:
            if node.getKey() >= x:
                L.append(node)
            node = self.next(node)
        return L

    def insert(self, key):
        """Inputs: key is a numerical value.
           Adds node with key key to the tree. Returns nothing.
        """
        parent = self.find(key)
        node = Node(key)
        node.setParent(parent)
        if key < parent.getKey():
            parent.setLeftChild(node)
        else:
            parent.setRightChild(node)
        while parent:
            parent.incrementSize()
            parent = parent.getParent()

    def delete(self, node):
        """Input: node object
           Removes the node from the tree.
           Returns nothing.
        """
        parent = node.getParent()
        left = node.getLeftChild()
        right = node.getRightChild()

        if not right:                                           # node doesn't have right child
            if not left and not parent:                         # "node" is the only node in the tree
                return None                                     # Returns nothing. We could set self.root to be None, but we would have a problem with printing (traversing) it, unless we changed the traversing methods - so, this leaves it in the tree
            if left:
                left.setParent(parent)
            if parent:
                if node.getKey() < parent.getKey():             # node is left child
                    parent.setLeftChild(left)
                elif node.getKey() > parent.getKey():           # node is right child
                    parent.setRightChild(left)
            else:                                               # We're deleting the root.
                self.root = left                                # Left becomes the new root.

        else:                                                   # node has right child
            X = self.next(node)                                 # meaning, x doesn't have left child
            Y = X.getRightChild()
            pX = X.getParent()

            if Y:
                if X != right:
                    Y.setParent(pX)
                    pX.setLeftChild(Y)
            else:
                pX.setLeftChild(None)

            if X != right:
                X.setRightChild(right)
                right.setParent(X)

            X.setParent(parent)
            if parent:                                          # We're not deleting the root.
                if node.getKey() < parent.getKey():             # node is left child
                    parent.setLeftChild(X)
                elif node.getKey() > parent.getKey():           # node is right child
                    parent.setRightChild(X)
            else:                                               # We're deleting the root.
                self.root = X                                   # X becomes new root.

            if left:
                X.setLeftChild(left)
                left.setParent(X)

        node.setParent(None)
        node.setLeftChild(None)
        node.setRightChild(None)
        del node

    def rotateRight(self, node):
        """Input: A node object that we want to rotate right.
           Returns nothing.
        """
        parent = node.getParent()
        Y = node.getLeftChild()
        if not Y:
            return None                                         # we can't rotate the node with nothing!
        B = Y.getRightChild()
        Y.setParent(parent)
        if parent:
                if node.getKey() < parent.getKey():             # node is left child
                    parent.setLeftChild(Y)
                elif node.getKey() > parent.getKey():           # node is right child
                    parent.setRightChild(Y)
        else:
            self.root = Y
        node.setParent(Y)
        Y.setRightChild(node)
        if B:
            B.setParent(node)
        node.setLeftChild(B)

    def rotateLeft(self, node):
        """Input: A node object that we want to rotate left.
           Returns nothing.
        """
        # we're just rotating back now, to the left
        parent = node.getParent()
        X = node.getRightChild()
        if not X:
            return None                                         # we can't rotate the node with nothing!
        B = X.getLeftChild()
        X.setParent(parent)
        if parent:
                if node.getKey() < parent.getKey():             # node is left child
                    parent.setLeftChild(X)
                elif node.getKey() > parent.getKey():           # node is right child
                    parent.setRightChild(X)
        else:
            self.root = X
        node.setParent(X)
        X.setLeftChild(node)
        if B:
            B.setParent(node)
        node.setRightChild(B)



def printTree(bst, verbose = False):
    """If boolean verbose is True, it will print(all nodes, in BFS order.
    """
    print()
    print("In order:  ", bst.inOrder())
    print("Pre order: ", bst.preOrder())
    print("BFS:       ", bst.BFS())
    if verbose:
        print("Nodes (in BFS order):")
        nodes = bst.BFS()
        for node in nodes:
            bst.find(node).printNode()
    print()