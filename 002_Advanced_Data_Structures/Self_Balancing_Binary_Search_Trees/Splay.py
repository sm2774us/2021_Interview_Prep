"""
UC Berkeley CS 61B: https://www.youtube.com/watch?v=G5QIXywcJlY&list=PL4BBB74C7D2A1049C&index=34
Wikipedia: https://en.wikipedia.org/wiki/Splay_tree
Also see http://www.cs.usfca.edu/~galles/visualization/SplayTree.html.

We do splay at the end of each operation because we might have found a very deep part of the tree which we do not want to have.
We want to speed things up in that part of the tree for the future.
But, some methods must not do splay at its end, because that would affect functioning of some other methods invoking them.
For instance, delete() calls _find(), _next() and _subtreeMinimum(), expecting all nodes to remain in their position, in order to work properly.
If needed, we can manually splay after such operation.
There are also two versions of method find(), for instance: private, _find(), and public, find().
We must use _find() in printTree()!
"""

from collections import deque


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
        return "Key: {}, Size: {}".format(self.key, self.size)



class SplayTree(object):

    def __init__(self):
        """Creates an empty splay tree."""
        self.root = None
        self.size = 0

    def __str__(self):
        return "Root = {}; Tree size = {}".format(repr(self.root), self.size)

    def __repr__(self):
        """Useful for debugging.
        The first part returns the original value of __repr__(), which contains type of the object and its address in memory.
        The second part gives us information about the root of the tree, which is its key, because it calls its __repr__() method.
        """
        return super(SplayTree, self).__repr__() + " Root = {}; Tree size = {}".format(repr(self.root), self.size)

    def _setRoot(self, node):
        self.root = node

    def getRoot(self):
        return self.root

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size

    def _inOrderRec(self, current):
        if current.getLeftChild():
            self._inOrderRec(current.getLeftChild())
        self.result.append(current.getKey())
        if current.getRightChild():
            self._inOrderRec(current.getRightChild())

    def inOrder(self):
        root = self.root
        if not root:
            return []
        self.result = []
        self._inOrderRec(root)
        return self.result

    def preOrder(self):
        root = self.root
        if not root:
            return []
        self.result = []
        stack = [root]                                          # stack contains nodes
        while stack:
            current = stack.pop()                               # an index
            self.result.append(current.getKey())
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
        self.result.append(current.getKey())

    def postOrder(self):
        root = self.root
        if not root:
            return []
        self.result = []
        self._postOrderRec(root)
        return self.result

    def levelOrder(self):                                       # Breadth First Search
        root = self.root
        if not root:
            return []
        self.result = []
        queue = deque([root])                                   # queue contains nodes
        while queue:
            current = queue.popleft()
            self.result.append(current.getKey())
            if current.getLeftChild():
                queue.append(current.getLeftChild())
            if current.getRightChild():
                queue.append(current.getRightChild())
        return self.result

    def _subtreeMinimum(self, node):
        """
        Input: Node object in the tree.
        Returns a node object with minimum key value in the subtree rooted at node.
        Doesn't splay any node.
        """
        if not node:
            return None
        while node.getLeftChild():
            node = node.getLeftChild()
        return node

    def _subtreeMaximum(self, node):
        """
        Input: Node object in the tree.
        Returns a node object with maximum key value in the subtree rooted at node.
        Doesn't splay any node.
        """
        if not node:
            return None
        while node.getRightChild():
            node = node.getRightChild()
        return node

    def _next(self, node):
        """Input is a node object.
           Outputs the next node object in terms of key value, or None, if we input the largest one.
           Doesn't splay any node.
        """
        right = node.getRightChild()
        if right:
            return self._leftDescendant(right)
        else:
            return self._rightAncestor(node)

    def _leftDescendant(self, node):
        left = node.getLeftChild()
        if not left:
            return node
        else:
            return self._leftDescendant(left)

    def _rightAncestor(self, node):
        parent = node.getParent()
        if parent:
            if node == parent.getLeftChild():
                return parent
            else:
                return self._rightAncestor(parent)
        else:
            return None

    def _previous(self, node):
        """Input is a node object.
           Outputs the previous node object in terms of key value, or None, if we input the smallest one.
           Doesn't splay any node.
        """
        if node.getLeftChild():
            return self._rightDescendant(node.getLeftChild())
        else:
            return self._leftAncestor(node)

    def _rightDescendant(self, node):
        right = node.getRightChild()
        if not right:
            return node
        else:
            return self._rightDescendant(right)

    def _leftAncestor(self, node):
        parent = node.getParent()
        if parent:
            if node == parent.getRightChild():
                return parent
            else:
                return self._leftAncestor(parent)
        else:
            return None

    def _rotateRight(self, node):
        """Input: A node object that we want to rotate right.
           Returns nothing.
           Doesn't splay any node.
        """
        parent = node.getParent()
        Y = node.getLeftChild()
        if not Y:
            return None                                         # we can't rotate the node with nothing!
        B = Y.getRightChild()
        Y.setParent(parent)
        if parent:
            if node == parent.getLeftChild():                   # node is left child
                parent.setLeftChild(Y)
            else:                                               # node is right child
                parent.setRightChild(Y)
        else:
            self.root = Y

        node.setParent(Y)
        Y.setRightChild(node)
        if B:
            B.setParent(node)
        node.setLeftChild(B)

        self._recomputeSize(node)
        self._recomputeSize(Y)

    def _rotateLeft(self, node):
        """Input: A node object that we want to rotate left.
           Returns nothing.
           Doesn't splay any node.
        """
        parent = node.getParent()
        X = node.getRightChild()
        if not X:
            return None                                         # we can't rotate the node with nothing!
        B = X.getLeftChild()
        X.setParent(parent)
        if parent:
            if node == parent.getLeftChild():                   # node is left child
                parent.setLeftChild(X)
            else:                                               # node is right child
                parent.setRightChild(X)
        else:
            self.root = X

        node.setParent(X)
        X.setLeftChild(node)
        if B:
            B.setParent(node)
        node.setRightChild(B)

        self._recomputeSize(node)
        self._recomputeSize(X)

    def _recomputeSize(self, node):
        """Doesn't splay any node."""
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

    def _splay(self, node):
        """
        Splays node to the top of the tree, making it new root of the tree.
        Returns nothing.
        """
        if not node:
            return

        parent = node.getParent()

        while parent:

            left = node.getLeftChild()
            right = node.getRightChild()
            grandParent = parent.getParent()
            if grandParent:
                greatGrandParent = grandParent.getParent()

            # Zig
            if not grandParent:
                if node == parent.getLeftChild():
                    self._rotateRight(parent)
                else:
                    self._rotateLeft(parent)

            # Zig-zig
            elif node == parent.getLeftChild() and parent == grandParent.getLeftChild():
                self._rotateRight(grandParent)
                self._rotateRight(parent)

            elif node == parent.getRightChild() and parent == grandParent.getRightChild():
                self._rotateLeft(grandParent)
                self._rotateLeft(parent)

            # Zig-zag
            elif node == parent.getLeftChild() and parent == grandParent.getRightChild():
                self._rotateRight(parent)
                self._rotateLeft(grandParent)

            else:
                self._rotateLeft(parent)
                self._rotateRight(grandParent)

            parent = node.getParent()

    def _find(self, key):
        """Inputs: key is a numerical value.
           Returns a node object - if the key (value) is found exactly, than it returns that node, otherwise it returns the node under which the searched key should be.
           If the tree is empty, returns None.
           This is a private method, which doesn't splay the found node to the top of the tree. This is a standard BST find() method.
        """
        node = self.root
        while node:
            if node.getKey() == key:
                break
            elif node.getKey() > key:
                if node.getLeftChild():
                    node = node.getLeftChild()
                    continue
                break
            else:                                               # node.getKey() < key:
                if node.getRightChild():
                    node = node.getRightChild()
                    continue
                break
        return node

    def find(self, key):
        """Inputs: key is a numerical value.
           Returns a node object - if the key (value) is found exactly, then it returns that node, otherwise it returns the node under which the searched key should be.
           If the tree is empty, returns None.
           This is a public method, which splays the found node to the top of the tree.
        """
        node = self.root
        while node:
            if node.getKey() == key:
                break
            elif node.getKey() > key:
                if node.getLeftChild():
                    node = node.getLeftChild()
                    continue
                break
            else:                                               # node.getKey() < key:
                if node.getRightChild():
                    node = node.getRightChild()
                    continue
                break
        self._splay(node)
        return node

    def insert(self, key):
        """Input: key is a numerical value.
           Adds node with key key to the tree, and splays it up to the top of the tree.
           Returns nothing.           
           Goes down the tree only once, and also goes up just once.
        """
        self.size += 1
        parent = self._find(key)
        node = Node(key)
        if not parent:
            self.root = node
            return
        node.setParent(parent)
        if key < parent.getKey():
            parent.setLeftChild(node)
        else:
            parent.setRightChild(node)
        self._splay(node)
        #node.recomputeSize()                                   # no need - this is done in _rotateLeft() and _rotateRight()

    def insertTree(self, root):
        """Input: root is a tree's root node object.
           Adds whole Splay tree rooted at root to an empty Splay tree. This method is used in function split().
           Returns nothing.
        """
        self.size = root.getSize()
        self.root = root

    def delete(self, key):
        """Input: key is a numerical value.
           If a node with the key is found, removes the node from the tree.
           If it isn't found, nothing happens.
           Returns nothing.
        """
        node = self._find(key)

        if not node:                                            # The tree is empty.
            return None                                         # Returns nothing.

        if node.getKey() != key:                                # The key is not in the tree.
            self._splay(node)                                   # We will splay that node nevertheless.
            return None                                         # Returns nothing.

        self._splay(node)

        self.size -= 1
        parent = node.getParent()
        left = node.getLeftChild()
        right = node.getRightChild()

        if left and right:                                      # node has two children
            X = self._subtreeMinimum(right)                     # meaning, X doesn't have left child
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

            X.setParent(None)                                   # for garbage collector
            X.setRightChild(None)                               # for garbage collector
            del X                                               # we are deleting X from the tree, not node - but X's key was copied to node - for garbage collector

        elif left:                                              # node has exactly one child, left
            ##### Never enters this if block - parent is always None here! #####
            if parent:                                          ##### Never enters this if block - parent is always None here! #####
                if node == parent.getLeftChild():               # node is left child
                    parent.setLeftChild(left)
                else:
                    parent.setRightChild(left)                  # node is right child
                node.setParent(None)
            ##### Never enters this if block - parent is always None here! #####
            else:                                               # we're deleting the root
                self.root = left                                # we're deleting the root; left becomes the new root
            left.setParent(parent)
            node.setLeftChild(None)                             # for garbage collector
            del node                                            # we are deleting the node - for garbage collector

        elif right:                                             # node has exactly one child, right
            ##### Never enters this if block - parent is always None here! #####
            if parent:                                          ##### Never enters this if block - parent is always None here! #####
                if node == parent.getLeftChild():               # node is left child
                    parent.setLeftChild(right)
                else:
                    parent.setRightChild(right)                 # node is right child
                node.setParent(None)
            ##### Never enters this if block - parent is always None here! #####
            else:                                               # we're deleting the root
                self.root = right                               # we're deleting the root; right becomes the new root
            right.setParent(parent)
            node.setRightChild(None)                            # for garbage collector
            del node                                            # we are deleting the node - for garbage collector

        else:                                                   # node has zero children, it's a leaf
            ##### Never enters this if block - parent is always None here! #####
            if parent:                                          ##### Never enters this if block - parent is always None here! #####
                if node == parent.getLeftChild():               # node is left child
                    parent.setLeftChild(None)
                else:
                    parent.setRightChild(None)                  # node is right child
                node.setParent(None)
            ##### Never enters this if block - parent is always None here! #####
            else:                                               # node is the only node in the tree
                self.root = None                                # node is the only node in the tree
                return None                                     # Returns nothing.

        ##### Never enters this while loop - parent is always None here! #####
        while parent:                                           ##### Never enters this while loop - parent is always None here! #####
            parent.decrementSize()
            parent = parent.getParent()
        ##### Never enters this while loop - parent is always None here! #####

    def subtreeMinimum(self, node):
        """
        Input: Node object in the tree.
        Returns a node object with minimum key value in the subtree rooted at node.
        Splays the found node to the top of the tree.
        """
        if not node:
            return None
        while node.getLeftChild():
            node = node.getLeftChild()
        self._splay(node)
        return node

    def subtreeMaximum(self, node):
        """
        Input: Node object in the tree.
        Returns a node object with maximum key value in the subtree rooted at node.
        Splays the found node to the top of the tree.
        """
        if not node:
            return None
        while node.getRightChild():
            node = node.getRightChild()
        self._splay(node)
        return node

    def next(self, key):
        """Input is an integer key.
           Outputs the next node object in terms of key value, or None, if we input the largest one.
           Splays the node with key key to the top of the tree.
        """
        node = self.find(key)
        right = node.getRightChild()
        if right:
            return self._leftDescendant(right)
        else:
            return self._rightAncestor(node)

    def next(self, key):
        """Input is an integer key.
           Outputs the next node object in terms of key value, or None, if we input the largest one.
           Splays the node with the key key to the top of the tree, and makes the next node its right child.
        """
        node = self._find(key)
        right = node.getRightChild()
        if right:
            nxt = self._leftDescendant(right)
            self._splay(nxt)
            self.find(key)
            return nxt
        else:
            nxt = self._rightAncestor(node)
            self._splay(nxt)
            self.find(key)
            return nxt

    def rangeSearch(self, x, y):
        """Inputs: numbers x, y
           Output: A list of nodes with key between x and y
        """
        L = []
        node = self.find(x)
        while node and node.getKey() <= y:
            if node.getKey() >= x:
                L.append(node)
            node = self._next(node)
        return L

    def _orderStatisticZeroBasedRankingRecursive(self, R, k):
        """
        Input: Root R of the tree (a node object); Integer number k - the rank of a node (0 <= k < size of the whole tree).
        Output: The k-th smallest element in the tree (a node object). Counting starts from 0.
        This is a private method, which doesn't splay the found node to the top of the tree.
        If needed, we should splay it manually after a call to this method.
        """
        assert 0 <= k < self.getSize(), "0 <= k < size of the whole tree"
        left, right = R.getLeftChild(), R.getRightChild()
        s = left.getSize() if left else 0
        if k == s:
            return R
        elif k < s:
            return self._orderStatisticZeroBasedRankingRecursive(left, k)
        elif k > s:
            return self._orderStatisticZeroBasedRankingRecursive(right, k - s - 1)

    def _orderStatisticZeroBasedRanking(self, k):
        """
        Input: Integer number k - the rank of a node (0 <= k < size of the whole tree).
        Output: The k-th smallest element in the tree (a node object). Counting starts from 0.
        This is a private method, which doesn't splay the found node to the top of the tree.
        If needed, we should splay it manually after a call to this method.
        """
        assert 0 <= k < self.getSize(), "0 <= k < size of the whole tree"
        node = self.getRoot()
        while node:
            left, right = node.getLeftChild(), node.getRightChild()
            s = left.size if left else 0
            if k == s:
                break
            elif k < s:
                if left:
                    node = left
                    continue
                break
            else:
                if right:
                    k = k - s - 1
                    node = right
                    continue
                break
        return node

    def orderStatisticZeroBasedRanking(self, k):
        """
        Input: Integer number k - the rank of a node (0 <= k < size of the whole tree).
        Output: The k-th smallest element in the tree (a node object). Counting starts from 0.
        This is a public method, which splays the found node to the top of the tree.
        """
        assert 0 <= k < self.getSize(), "0 <= k < size of the whole tree"
        node = self.getRoot()
        while node:
            left, right = node.getLeftChild(), node.getRightChild()
            s = left.size if left else 0
            if k == s:
                break
            elif k < s:
                if left:
                    node = left
                    continue
                break
            else:
                if right:
                    k = k - s - 1
                    node = right
                    continue
                break
        self._splay(node)
        return node

    def _orderStatisticRecursive(self, R, k):
        """
        Input: Root R of the tree (a node object); Integer number k - the rank of a node (1 <= k <= size of the whole tree).
        Output: The k-th smallest element in the tree (a node object). Counting starts from 1.
        This is a private method, which doesn't splay the found node to the top of the tree.
        If needed, we should splay it manually after a call to this method.
        """
        assert 1 <= k <= self.getSize(), "1 <= k <= size of the whole tree"
        left, right = R.getLeftChild(), R.getRightChild()
        if left:
            s = left.getSize()
        else:
            s = 0
        if k == s + 1:
            return R
        elif k < s + 1:
            return self._orderStatisticRecursive(left, k)
        elif k > s + 1:
            return self._orderStatisticRecursive(right, k - s - 1)

    def _orderStatistic(self, k):
        """
        Input: Integer number k - the rank of a node (1 <= k <= size of the whole tree).
        Output: The k-th smallest element in the tree (a node object). Counting starts from 1.
        This is a private method, which doesn't splay the found node to the top of the tree.
        If needed, we should splay it manually after a call to this method.
        """
        assert 1 <= k <= self.getSize(), "1 <= k <= size of the whole tree"
        node = self.getRoot()
        while node:
            left, right = node.getLeftChild(), node.getRightChild()
            s = left.size if left else 0
            if k == s + 1:
                break
            elif k < s + 1:
                if left:
                    node = left
                    continue
                break
            else:
                if right:
                    k = k - s - 1
                    node = right
                    continue
                break
        return node

    def orderStatistic(self, k):
        """
        Input: Integer number k - the rank of a node (1 <= k <= size of the whole tree).
        Output: The k-th smallest element in the tree (a node object). Counting starts from 1.
        This is a public method, which splays the found node to the top of the tree.
        """
        assert 1 <= k <= self.getSize(), "1 <= k <= size of the whole tree"
        node = self.getRoot()
        while node:
            left, right = node.getLeftChild(), node.getRightChild()
            s = left.size if left else 0
            if k == s + 1:
                break
            elif k < s + 1:
                if left:
                    node = left
                    continue
                break
            else:
                if right:
                    k = k - s - 1
                    node = right
                    continue
                break
        self._splay(node)
        return node

    def computeRank(self, R, key):
        """
        Input: Root R of the tree (a node object); a key of a node in the tree (a number).
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
            prev = self._previous(R)
            p = 1
            while prev:
                prevKey = prev.getKey()
                if prevKey == key:
                    return leftSize + 1 - p
                elif prevKey < key:
                    return "Key {} not found, but it would have the rank of {}.".format(key, leftSize + 2 - p)
                prev = self._previous(prev)
                p += 1
            return "Key {} not found, but it would have the rank of {}.".format(key, leftSize + 2 - p)
        elif key > R.getKey():
            next = self._next(R)
            n = 1
            while next:
                nextKey = next.getKey()
                if nextKey == key:
                    return leftSize + 1 + n
                elif nextKey > key:
                    return "Key {} not found, but it would have the rank of {}.".format(key, leftSize + 1 + n)
                next = self._next(next)
                n += 1
            return "Key {} not found, but it would have the rank of {}.".format(key, leftSize + 1 + n)



def merge(tree1, tree2):
    """Merges two Splay trees, tree1 and tree2, using the largest element in tree1 as the node for merging, into a new Splay tree.
    CONSTRAINTS: All keys in tree1 must be smaller than all keys in tree2.
    INPUTS: tree1, tree2.
    OUTPUT (the return value of this function) is tree1, with all the elements of both trees.
    USAGE: After this function, we can delete tree2.
    """
    if not tree1 or not tree1.getRoot():
        return tree2
    if not tree2 or not tree2.getRoot():
        return tree1
    root2 = tree2.getRoot()
    root1 = tree1.find(float("inf"))                            # same as root1 = tree1.subtreeMaximum(tree1.getRoot())
    root1.setRightChild(root2)
    root2.setParent(root1)
    root1.recomputeSize()
    tree1.setSize(root1.getSize())
    return tree1


def split(tree, x):
    """
    Splits Splay tree into two trees.
    Input: A Splay tree; key x.
    Output: Two Splay trees, one with elements <= x, the other with elements > x.
    Usage: User can delete node with key x from the left tree (tree1) after getting the trees, in case they want to remove x from the first tree as well,
    so that they have only elements < x, and not <= x ( tree1.delete(x) ).
    Also, user can delete the original tree.
    """
    if not tree or not tree.getRoot():
        return None
    root1 = tree.find(x)
    if root1.getKey() > x:
        root1 = tree.subtreeMaximum(root1.getLeftChild())
    if not root1:
        tree.setSize(tree.getRoot().getSize())
        return SplayTree(), tree
    root2 = root1.getRightChild()
    root1.setRightChild(None)
    root1.recomputeSize()
    tree1 = SplayTree()
    tree1.insertTree(root1)
    tree2 = SplayTree()        
    if root2:
        root2.setParent(None)
        tree2.insertTree(root2)
    return tree1, tree2


def printTree(tree, verbose = False):
    """If boolean verbose is True, it will print(all nodes, in level order (BFS).
       We must use _find() in printTree()!
    """
    print()
    print("In order:   ", tree.inOrder())
    print("Pre order:  ", tree.preOrder())
    print("Level order:", tree.levelOrder())
    if verbose:
        print("Nodes (in level order (BFS)):")
        nodes = tree.levelOrder()
        for node in nodes:
            tree._find(node).printNode()
    print()
