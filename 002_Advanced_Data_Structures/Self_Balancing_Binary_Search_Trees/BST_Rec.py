"""
Recursive version

Contains methods for tree traversal.
This version assumes that keys of all nodes in a tree are different, that they don't repeat.
This also helps:
https://en.wikipedia.org/wiki/Binary_search_tree
https://en.wikipedia.org/wiki/Tree_rotation
http://www.cs.usfca.edu/~galles/visualization/BST.html
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

    def setRoot(self, node):
        self.root = node

    def getRoot(self):
        return self.root

    def _inOrderRec(self, current):
        if current.getLeftChild():
            self._inOrderRec(current.getLeftChild())
        self.result.append(current.getKey())                    # visit()
        if current.getRightChild():
            self._inOrderRec(current.getRightChild())

    def inOrderR(self, root):
        """Input: root is a node to begin traversing the tree with. It doesn't have to be the root of the whole tree.
        Returns the visited nodes' keys in post-order traversal, as a list.
        Works recursively."""
        self.result = []
        self._inOrderRec(root)
        return self.result

    def inOrder(self, root):                                    # Iterative
        """Input: root is a node to begin traversing the tree with. It doesn't have to be the root of the whole tree.
        Returns the visited nodes' keys in in-order traversal, as a list.
        Works iteratively."""
        current = root
        if not current:
            return []
        self.result = []
        stack = []                                              # stack contains nodes
        while True:
            while current:
                stack.append(current)
                current = current.left
            if stack:
                current = stack.pop()
                self.result.append(current.getKey())            # visit()
                current = current.right
            else:
                return self.result

    def preOrder(self, root):                                   # Iterative
        """Input: root is a node to begin traversing the tree with. It doesn't have to be the root of the whole tree.
        Returns the visited nodes' keys in pre-order traversal, as a list.
        Works iteratively."""
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

    def _postOrderRec(self, current):
        if current.getLeftChild():
            self._postOrderRec(current.getLeftChild())
        if current.getRightChild():
            self._postOrderRec(current.getRightChild())
        self.result.append(current.getKey())                    # visit()

    def postOrderR(self, root):
        """Input: root is a node to begin traversing the tree with. It doesn't have to be the root of the whole tree.
        Returns the visited nodes' keys in post-order traversal, as a list.
        Works recursively."""
        self.result = []
        self._postOrderRec(root)
        return self.result

    def postOrder(self, root):                                  # Iterative
        """Input: root is a node to begin traversing the tree with. It doesn't have to be the root of the whole tree.
        Returns the visited nodes' keys in post-order traversal, as a list.
        Works iteratively."""
        self.result = []
        stack = []                                              # stack contains nodes
        boolStack = []                                          # For each element on the node stack, a corresponding value is stored on the bool stack. If this value is true, then we need to pop and visit the node on next encounter.
        current = root
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

    def BFS(self, root):                                        # Iterative
        """Input: root is a node to begin traversing the tree with. It doesn't have to be the root of the whole tree.
        Returns the visited nodes' keys in level-order traversal, as a list.
        Works iteratively."""
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

    def find(self, key, root):
        """Inputs: key is a numerical value.
           root is the root node object.
           Returns a node object - if the key (value) is found exactly, than it returns that node, otherwise it returns the node under which the searched key should be.
        """
        # Only in the first call will the root be the root node object; in subsequent calls it will actually be a node object, but not the root anymore.
        if root.getKey() == key:
            return root
        elif root.getKey() > key:
            if root.getLeftChild():
                return self.find(key, root.getLeftChild())
            return root
        elif root.getKey() < key:
            if root.getRightChild():
                return self.find(key, root.getRightChild())
            return root

    def findMin(self, root):
        """
        Input: Root node object of the tree.
        Returns a node object with minimal key value in the tree (the first element of the tree).
        """
        return self.find(float("-inf"), root)

    def findMax(self, root):
        """
        Input: Root node object of the tree.
        Returns a node object with maximal key value in the tree (the last element of the tree).
        """
        return self.find(float("inf"), root)

    def subtreeMinimum(self, node):
        """
        Input: Node object in the tree.
        Returns a node object with minimal key value in the subtree rooted at node.
        """
        if not node:
            return None
        while node.getLeftChild():
            node = node.getLeftChild()
        return node

    def subtreeMaximum(self, node):
        """
        Input: Node object in the tree.
        Returns a node object with maximal key value in the subtree rooted at node.
        """
        if not node:
            return None
        while node.getRightChild():
            node = node.getRightChild()
        return node

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

    def rangeSearch(self, x, y, root):
        """Inputs: numbers x, y; root object
           Output: A list of nodes with key between x and y
        """
        L = []
        node = self.find(x, root)
        while node and node.getKey() <= y:
            if node.getKey() >= x:
                L.append(node)
            node = self.next(node)
        return L

    def insert(self, key, root):
        """Inputs: key is a numerical value; root is the root node object.
           Adds node with key key to the tree. Returns nothing.
           Node is always inserted as a leaf, so its size is 1.
        """
        parent = self.find(key, root)
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
           Returns the tree's root object.
        """
        parent = node.getParent()
        left = node.getLeftChild()
        right = node.getRightChild()

        if not right:                                           # node doesn't have right child
            if not left and not parent:                         # "node" is the only node in the tree
                return self.root                                # we could set self.root to be None, but we would have a problem with printing (traversing) it, unless we changed the traversing methods - so, this leaves it in the tree
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
            X = self.next(node)                                 # meaning, X doesn't have left child
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
                while pX != X:
                    pX.decrementSize()
                    pX = pX.getParent()

            if left:
                X.setLeftChild(left)
                left.setParent(X)

            X.setParent(parent)
            if parent:                                          # We're not deleting the root.
                if node.getKey() < parent.getKey():             # node is left child
                    parent.setLeftChild(X)
                elif node.getKey() > parent.getKey():           # node is right child
                    parent.setRightChild(X)
            else:                                               # We're deleting the root.
                self.root = X                                   # X becomes new root.

            self.recomputeSize(X)

        while parent:
            parent.decrementSize()
            parent = parent.getParent()

        node.setParent(None)
        node.setLeftChild(None)
        node.setRightChild(None)
        del node                                                # we are deleting the node
        return self.root

    def deleteKey(self, key):                                   # based on UC Berkeley CS 61B
        """Input: key is a numerical value.
           If a node with the key is found, removes the node from the tree.
           If it isn't found, nothing happens.
           Returns the tree's root object if the key is found, or None if the key isn't found in the tree.
        """
        node = self.find(key, self.root)

        if node.getKey() != key:                                # The key is not in the tree.
            return None                                         # Returns None if it hasn't found the key.

        parent = node.getParent()
        left = node.getLeftChild()
        right = node.getRightChild()

        if left and right:                                      # node has two children
            X = self.subtreeMinimum(right)                      # meaning, X doesn't have left child
            pX = X.getParent()
            Xright = X.getRightChild()

            node.setKey(X.getKey())                             # we're leaving the node that we wanted to delete in the tree, but we change its key to be the X's key (which is also done at https://en.wikipedia.org/wiki/Binary_search_tree)

            if Xright:
                Xright.setParent(pX)
            if X == right:                                      # meaning, node == pX
                node.setRightChild(Xright)
            else:
                pX.setLeftChild(Xright)

            while pX != node:
                pX.decrementSize()
                pX = pX.getParent()
            node.decrementSize()

            X.setParent(None)
            X.setRightChild(None)
            del X                                               # we are deleting X from the tree, not node - but X's key was copied to node

        elif left:                                              # node has exactly one child, left
            if parent:
                if node == parent.getLeftChild():               # node is left child
                    parent.setLeftChild(left)
                else:
                    parent.setRightChild(left)                  # node is right child
                node.setParent(None)
            else:                                               # we're deleting the root
                self.root = left                                # left becomes the new root
            left.setParent(parent)
            node.setLeftChild(None)
            del node                                            # we are deleting the node

        elif right:                                             # node has exactly one child, right
            if parent:
                if node == parent.getLeftChild():               # node is left child
                    parent.setLeftChild(right)
                else:
                    parent.setRightChild(right)                 # node is right child
                node.setParent(None)
            else:                                               # we're deleting the root
                self.root = right                               # left becomes the new root
            right.setParent(parent)
            node.setRightChild(None)
            del node                                            # we are deleting the node

        else:                                                   # node has zero children, it's a leaf
            if parent:
                if node == parent.getLeftChild():               # node is left child
                    parent.setLeftChild(None)
                else:
                    parent.setRightChild(None)                  # node is right child
                node.setParent(None)
            else:
                return self.root                                # we could set self.root to be None, but we would have a problem with printing (traversing) it, unless we changed the traversing methods - so, this leaves it in the tree

        while parent:
            parent.decrementSize()
            parent = parent.getParent()

        return self.root

    def rotateRight(self, node):
        """Input: A node object that we want to rotate right.
           Returns the tree's root object.
        """
        parent = node.getParent()
        Y = node.getLeftChild()
        if not Y:
            return self.root                                    # we can't rotate the node with nothing!
        B = Y.getRightChild()
        Y.setParent(parent)
        if parent:
            if node.getKey() < parent.getKey():                 # node is left child
                parent.setLeftChild(Y)
            elif node.getKey() > parent.getKey():               # node is right child
                parent.setRightChild(Y)
        else:
            self.root = Y

        node.setParent(Y)
        Y.setRightChild(node)
        if B:
            B.setParent(node)
        node.setLeftChild(B)

        self.recomputeSize(node)
        self.recomputeSize(Y)
        return self.root

    def rotateLeft(self, node):
        """Input: A node object that we want to rotate left.
           Returns the tree's root object.
        """
        # we're just rotating back now, to the left
        parent = node.getParent()
        X = node.getRightChild()
        if not X:
            return self.root                                    # we can't rotate the node with nothing!
        B = X.getLeftChild()
        X.setParent(parent)
        if parent:
            if node.getKey() < parent.getKey():                 # node is left child
                parent.setLeftChild(X)
            elif node.getKey() > parent.getKey():               # node is right child
                parent.setRightChild(X)
        else:
            self.root = X

        node.setParent(X)
        X.setLeftChild(node)
        if B:
            B.setParent(node)
        node.setRightChild(B)

        self.recomputeSize(node)
        self.recomputeSize(X)
        return self.root

    def recomputeSize(self, node):
        if not node:
            return
        left, right = node.getLeftChild(), node.getRightChild()
        if left:
            leftSize = left.getSize()
        else:
            leftSize = 0
        if right:
            rightSize = right.getSize()
        else:
            rightSize = 0
        node.setSize(leftSize + rightSize + 1)



def mergeWithRoot(tree1, tree2, T):
    """Merges two Binary Search Trees, tree1 and tree2, with roots R1 and R2, using an extra node T as root of the new tree.
    Constraints: All keys in R1's tree must be smaller than all keys in tree rooted at R2. Also, T's key has to be greater than all keys in R1's tree, and less than all the keys in R2's tree.
    Inputs are two trees (tree1 and tree2) and a node T.
    Output is a new tree, rooted at T, with all the elements of both trees, node T included.
    """
    if tree1:
        R1 = tree1.getRoot()
        T.setLeftChild(R1)
        R1.setParent(T) 
    if tree2:
        R2 = tree2.getRoot()
        T.setRightChild(R2)
        R2.setParent(T)
    T.recomputeSize()
    return BinarySearchTree(T)

def merge(tree1, tree2):
    """Merges two Binary Search Trees, tree1 and tree2, with roots R1 and R2, using the largest element in R1's tree as root of the new tree.
    Constraints: All keys in R1's tree must be smaller than all keys in tree rooted at R2.
    Inputs are two trees (tree1 and tree2).
    Output is a new tree, rooted at T, with all the elements of both trees.
    """
    if not tree1:
        return tree2
    R1 = tree1.getRoot()
    if not tree2:
        return tree1
    R2 = tree2.getRoot()
    T = tree1.find(float("inf"), R1)
    R1 = tree1.delete(T)                                        # we have to update R1, in case it was the largest key in tree1 when it got deleted - in case we are deleting the root
    if T == R1:                                                 # this means that T is the only node in tree1, i.e., tree1 has only that one node, which we don't delete, but we're not going to duplicate it now, either
        tree2.insert(R1.getKey(), R2)
        return tree2
    mergeWithRoot(tree1, tree2, T)
    return BinarySearchTree(T)


def mergeWithRootNodes(R1, R2, T):
    """Merges two Binary Search Trees, tree1 and tree2, with roots R1 and R2, using an extra node T as root of the new tree.
    Constraints: All keys in R1's tree must be smaller than all keys in tree rooted at R2. Also, T's key has to be greater than all keys in R1's tree, and less than all the keys in R2's tree.
    Inputs are three nodes: roots of tree1 and tree2 (R1 and R2), and a node T.
    Output is root of the new tree, T, with all the elements of both trees, node T included.
    Usage: Since this function actually returns a node, and not a tree, we should create an ArrayAVL tree rooted at the return value of this function. Then, we can delete tree1 and tree2 to free memory up.
    """
    assert T, "T must be != None"
    T.setLeftChild(R1)
    T.setRightChild(R2)
    if R1:
        assert R1.getKey() < T.getKey(), "R1 has to be < T"
        R1.setParent(T)
    if R2:
        assert T.getKey() < R2.getKey(), "T has to be < R2"
        R2.setParent(T)
    T.recomputeSize()
    return T

def mergeNodes(tree1, R1, tree2, R2):
    """Merges two Binary Search Trees, tree1 and tree2, with roots R1 and R2, using the largest element in R1's tree as root of the new tree.
    Constraints: All keys in R1's tree must be smaller than all keys in tree rooted at R2.
    Inputs are two trees (tree1 and tree2) and their roots (R1 and R2): tree1, R1, tree2, R2.
    Output is root of the new tree, T, with all the elements of both trees.
    Usage: Since this function actually returns a node, and not a tree, we should create an ArrayAVL tree rooted at the return value of this function. Then, we can delete tree1 and tree2 to free memory up.
    """
    if not R1:
        return R2
    if not R2:
        return R1
    T = tree1.find(float("inf"), R1)
    R1 = tree1.delete(T)                                        # we have to update R1, in case it was the largest key in tree1 when it got deleted - in case we are deleting the root
    if T == R1:                                                 # this means that T is the only node in tree1, i.e., tree1 has only that one node, which we don't delete, but we're not going to duplicate it now, either
        tree2.insert(R1.getKey(), R2)
        return R2
    mergeWithRootNodes(R1, R2, T)
    return T


def _splitRec(R, x):
    """
    Splits tree into two trees.
    Input: Root R of a tree; key x.
    Output: Roots of two trees, one with elements <= x, the other with elements > x.
    Usage: User should set parents of both trees' roots to None after creating the two trees rooted at those two roots, and this should be done in two separate try-except blocks,
    because a tree might be empty. Usage example: "try: tree1/2.getRoot().setParent(None) except: pass". Of course, this can alternatively be achieved by using two "if" clauses.
    Also, user can delete node with key x from the left tree (tree1) after creating the trees, and AFTER fixing the parents, in case they want to remove x from the first tree as well,
    so that they have only elements < x, and not <= x ( tree1.delete(tree1.find(x, tree1.getRoot())) ).
    """
    if not R:
        return (None, None)
    if x < R.getKey():
        (R1, R2) = _splitRec(R.getLeftChild(), x)
        R3 = mergeWithRootNodes(R2, R.getRightChild(), R)
        return (R1, R3)
    if x >= R.getKey():
        (R1, R2) = _splitRec(R.getRightChild(), x)
        R3 = mergeWithRootNodes(R.getLeftChild(), R1, R)
        return (R3, R2)

def split(R, x):
    """
    Splits tree into two trees.
    Input: Root R of a tree; key x.
    Output: Roots of two trees, one with elements <= x, the other with elements > x.
    Usage: User can delete node with key x from the left tree (tree1) after creating the trees, in case they want to remove x from the first tree as well,
    so that they have only elements < x, and not <= x ( tree1.delete(tree1.find(x, tree1.getRoot())) ).
    Also, user can delete the original tree to save memory.
    """
    if x == R.getKey():                                         # if we're splitting at root
        right = R.getRightChild()
        R.setRightChild(None)
        if right:
            right.setParent(None)
        R.recomputeSize()
        return R, right
    else:
        R1, R2 = _splitRec(R, x)
        if R1:
            R1.setParent(None)
        if R2:
            R2.setParent(None)
        return R1, R2

def splitLess(R, x):
    """
    Splits tree into two trees.
    Input: Root R of a tree; key x.
    Output: Roots of two trees, one with elements < x (thus "Less" in the name), the other with elements >= x.
    Usage: User can delete node with key x from the right tree (tree2) after creating the trees, in case they want to remove x from the second tree as well,
    so that they have only elements > x, and not >= x ( tree2.delete(tree2.find(x, tree2.getRoot())) ).
    Also, user can delete the original tree to save memory.
    """
    x -= 1
    return split(R,x)

def _splitLessRec(R, x):
    """
    Splits tree into two trees.
    Input: Root R of a tree; key x.
    Output: Roots of two trees, one with elements < x (thus "Less" in the name), the other with elements >= x.
    Usage: User should set parents of both trees' roots to None after creating the two trees rooted at those two roots, and this should be done in two separate try-except blocks,
    because a tree might be empty. Usage example: "try: tree1/2.getRoot().setParent(None) except: pass". Of course, this can alternatively be achieved by using two "if" clauses.
    Also, user can delete node with key x from the right tree (tree2) after creating the trees, and AFTER fixing the parents, in case they want to remove x from the second tree as well,
    so that they have only elements > x, and not >= x ( tree2.delete(tree2.find(x, tree2.getRoot())) ).
    """
    if not R:
        return (None, None)
    if x <= R.getKey():
        (R1, R2) = _splitLessRec(R.getLeftChild(), x)
        R3 = mergeWithRootNodes(R2, R.getRightChild(), R)
        return (R1, R3)
    if x > R.getKey():
        (R1, R2) = _splitLessRec(R.getRightChild(), x)
        R3 = mergeWithRootNodes(R.getLeftChild(), R1, R)
        return (R3, R2)

def splitLess(R, x):
    """
    Splits tree into two trees.
    Input: Root R of a tree; key x.
    Output: Roots of two trees, one with elements < x (thus "Less" in the name), the other with elements >= x.
    Usage: User can delete node with key x from the right tree (tree2) after creating the trees, in case they want to remove x from the second tree as well,
    so that they have only elements > x, and not >= x ( tree2.delete(tree2.find(x, tree2.getRoot())) ).
    Also, user can delete the original tree to save memory.
    """
    if x == R.getKey():
        left = R.getLeftChild()
        R.setLeftChild(None)
        if left:
            left.setParent(None)
        R.recomputeSize()
        return left, R
    else:
        R1, R2 = _splitLessRec(R, x)
        if R1:
            R1.setParent(None)
        if R2:
            R2.setParent(None)
        return R1, R2


def orderStatisticZeroBasedRanking(R, k):
    """
    Input: Root R of the tree (a node object); Integer number k - the rank of a node (0 <= k < size of the whole tree).
    Output: The k-th smallest element in the tree (a node object). Counting starts from 0.
    """
    assert 0 <= k < R.getSize(), "0 <= k < size of the whole tree"
    left, right = R.getLeftChild(), R.getRightChild()
    s = left.getSize() if left else 0
    if k == s:
        return R
    elif k < s:
        return orderStatisticZeroBasedRanking(left, k)
    elif k > s:
        return orderStatisticZeroBasedRanking(right, k - s - 1)

def orderStatistic(R, k):
    """
    Input: Root R of a tree T (a node object); number k, the rank of a node (1 <= k <= size of the whole tree).
    Output: The k-th smallest element in the tree T (a node object). Counting starts from 1.
    """
    assert 1 <= k <= R.getSize(), "1 <= k <= size of the whole tree"
    left, right = R.getLeftChild(), R.getRightChild()
    if left:
        s = left.getSize()
    else:
        s = 0
    if k == s + 1:
        return R
    elif k < s + 1:
        return orderStatistic(left, k)
    elif k > s + 1:
        return orderStatistic(right, k - s - 1)

def computeRank(R, T, key):
    """
    Input: Root R (a node object) of a tree T (a tree object) and a key of a node in the tree (a number).
    Output: Rank of the node with the key "key" in the tree - a number.
    """
    left, right = R.getLeftChild(), R.getRightChild()
    if left:
        leftSize = left.getSize()
    else:
        leftSize = 0
    if right:
        rightSize = right.getSize()
    else:
        rightSize = 0
    if key == R.getKey():
        return leftSize + 1
    elif key < R.getKey():
        prev = T.previous(R)
        p = 1
        while prev:
            prevKey = prev.getKey()
            if prevKey == key:
                return leftSize + 1 - p
            elif prevKey < key:
                return "Key {} not found, but it would have the rank of {}.".format(key, leftSize + 2 - p)
            prev = T.previous(prev)
            p += 1
        return "Key {} not found, but it would have the rank of {}.".format(key, leftSize + 2 - p)
    elif key > R.getKey():
        next = T.next(R)
        n = 1
        while next:
            nextKey = next.getKey()
            if nextKey == key:
                return leftSize + 1 + n
            elif nextKey > key:
                return "Key {} not found, but it would have the rank of {}.".format(key, leftSize + 1 + n)
            next = T.next(next)
            n += 1
        return "Key {} not found, but it would have the rank of {}.".format(key, leftSize + 1 + n)


def printTree(bst, verbose = False):
    """If boolean verbose is True, it will print(all nodes, in BFS order.
       We can safely assign bst.getRoot() to root variable here, and work with it every time, because this function doesn't modify the tree;
       it only reads it, and prints it in-order, pre-order, and breadth first (level order).
       But, in other cases, we should be careful, and it's better to use bst.getRoot() every time. It's probably slower, but safer, and more elegant.
    """
    root = bst.getRoot()
    print()
    print("In order:   ", bst.inOrder(root))
    print("Pre order:  ", bst.preOrder(root))
    print("Level order:", bst.BFS(root))
    if verbose:
        print("Nodes (in Level/BFS order):")
        nodes = bst.BFS(root)
        for node in nodes:
            bst.find(node, root).printNode()
    print()
