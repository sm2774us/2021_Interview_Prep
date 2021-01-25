"""
This is an application of Binary Search Trees.
It's used for storing an array in a tree (or two trees), and it was invented to speed things up.
Uses 1-based indexing.
By using AVL trees like here (self balancing trees in general), we keep the maximum height of a tree at O(log n), so all operations on the array take at most O(log n) time.
Non-balancing BST has O(n) time complexity in the worst case, like a regular array (list).
"""

import AVL_Rec as AVL


class ArrayNode(AVL.AVLNode):

    def __init__(self, key, height, color):
        assert key and height and (color == 'b' or color == 'w'), "Node must be added with key and height and color ('b' or 'w')!"
        self.color = color
        return super(ArrayNode, self).__init__(key)

    def setColor(self, color):
        assert color == 'b' or color == 'w', "Color can be either 'b' or 'w'!"
        self.color = color

    def getColor(self):
        return self.color

    def printNode(self):
        print("Key: {}, Parent: {}, Left child: {}, Right child: {}, Size: {}, Height: {}, Color: {}".format(self.key, self.parent, self.left, self.right, self.size, self.height, repr(self.color)))

    def __str__(self):
        return str((self.key, self.color))

    def __repr__(self):
        """This can be used as:
           print(repr(tree.find(key, root)))
           But, it's also very useful for debugging, because debugger will show us the key of the node without the need for expanding the node.
           Of course, we can add some other pieces of information, too.
           We can return "str(self.key)" and concatenate other string to it, or we can use the form below. Anyhow, we must return a string.
        """
        return "Key: {}, Size: {}, Height: {}, Color: {}".format(self.key, self.size, self.height, repr(self.color))


class ArrayAVL(AVL.AVLTree):

    def __init__(self, root):
        """Expects a root node object as input."""
        return super(ArrayAVL, self).__init__(root)

    def __str__(self):
        return str(self.inOrder(self.root))

    def inOrderRec(self, current):
        if current.getLeftChild():
            self.inOrderRec(current.getLeftChild())
        self.result.append((current.getKey(), current.getColor()))
        if current.getRightChild():
            self.inOrderRec(current.getRightChild())

    def insert(self, key, color, root):
        """Inputs: key is a numerical value; color is 'b' or 'w'; root is the root node object.
           Adds ArrayNode with key key and color color to the ArrayAVL tree.
           Returns nothing.
           Node is always inserted as a leaf, so its size and height are 1.
           I had to override method insert() from BinarySearchTree() class because it creates a Node object which doesn't contain the color field.
        """
        parent = self.find(key, root)
        node = ArrayNode(key, 1, color)
        node.setParent(parent)
        if key < parent.getKey():
            parent.setLeftChild(node)
        else:
            parent.setRightChild(node)
        while parent:
            parent.incrementSize()
            parent = parent.getParent()

    def AVLInsert(self, key, color, root):
        """Inputs: key is a numerical value; color is 'b' or 'w'; root is the root node object.
           Adds AVL node with key key and color color to the tree. Returns nothing.
        """
        self.insert(key, color, root)
        node = self.find(key, root)
        self.rebalance(node)


class Array(object):
    """
    Array object of elements with color 'b' or 'w'.
    At the time of creation, all elements have color 'w'.
    """

    def __init__(self, n):
        """
        Creates an Array object of n elements with color 'w'.
        """
        self.size = n
        self.T1, self.T2 = self.newArray(self.size)

    def __str__(self):
        return str(self.T1)

    def getSize(self):
        return self.size

    def decrementSize(self):
        assert self.size > 1, "Size must be at least 1!"
        self.size -= 1

    def incrementSize(self):
        self.size += 1

    def oppositeColor(self, color):
        assert color == 'b' or color == 'w', "Color can be either 'b' or 'w'!"
        if color == 'b':
            return 'w'
        else:
            return 'b'

    def push(self, color):
        """
        Pushes a new element with color 'color' to the end of the array.
        Returns nothing.
        """
        self.incrementSize()
        self.T1.AVLInsert(self.size, color, self.T1.getRoot())
        self.T2.AVLInsert(self.size, self.oppositeColor(color), self.T2.getRoot())

    def pop(self):
        """
        Pops an element from the end of the array and returns it.
        """
        el1 = self.T1.find(self.size, self.T1.getRoot())
        self.T1.AVLDelete(el1)
        el2 = self.T2.find(self.size, self.T2.getRoot())
        self.T2.AVLDelete(el2)
        self.decrementSize()
        return el1

    def newArray(self, n):
        """
        Creates two ArrayBST trees, T1 and T2, with keys [1, n].
        All nodes in T1 have color 'w' (white), and all nodes in T2 have color 'b' (black).
        Returns T1, T2.
        """
        T1 = ArrayAVL(ArrayNode(1, 1, 'w'))
        for i in range(2, n + 1):
            T1.AVLInsert(i, 'w', T1.getRoot())

        T2 = ArrayAVL(ArrayNode(1, 1, 'b'))
        for i in range(2, n + 1):
            T2.AVLInsert(i, 'b', T2.getRoot())

        return T1, T2

    def getElement(self, m):
        """
        Returns color ('b' or 'w') of the m-th element in T1 (the Array).
        m has to be >= 1 and <= size.
        """
        assert 1 <= m <= self.size, "m has to be >= 1 and <= size!"
        el = self.T1.find(m, self.T1.getRoot())
        return el

    def setColor(self, m, color):
        """
        Sets color ('b' or 'w') of the m-th element in T1 (the Array), and the opposite color of the m-th element in T2.
        m has to be >= 1 and <= size.
        Returns nothing.
        """
        assert 1 <= m <= self.size, "m has to be >= 1 and <= size!"
        el1 = self.T1.find(m, self.T1.getRoot())
        el2 = self.T2.find(m, self.T2.getRoot())
        el1.setColor(color)
        el2.setColor(self.oppositeColor(color))

    def getColor(self, m):
        """
        Returns color ('b' or 'w') of the m-th element in T1 (the Array).
        m has to be >= 1 and <= size.
        """
        assert 1 <= m <= self.size, "m has to be >= 1 and <= size!"
        el = self.T1.find(m, self.T1.getRoot())
        return repr(el.getColor())

    def toggle(self, x):
        """
        Toggles color of the element with index x.
        x has to be >= 1 and <= size.
        Returns nothing.
        """
        assert 1 <= x <= self.size, "x has to be >= 1 and <= size!"
        el1 = self.T1.find(x, self.T1.getRoot())
        el2 = self.T2.find(x, self.T2.getRoot())
        color = el1.getColor()
        el1.setColor(self.oppositeColor(color))
        el2.setColor(color)

    def flip(self, x):
        """
        Flips color of all elements with index >= x.
        x has to be >= 1 and <= size.
        Returns nothing.
        """
        assert 1 <= x <= self.size, "x has to be >= 1 and <= size!"
        x -= 1
        L1, R1 = ArrayAVLSplit(self.T1, self.T1.getRoot(), x)
        L2, R2 = ArrayAVLSplit(self.T2, self.T2.getRoot(), x)
        L1Tree = ArrayAVL(L1)
        L2Tree = ArrayAVL(L2)
        R1Tree = ArrayAVL(R1)
        R2Tree = ArrayAVL(R2)
        self.T1 = ArrayAVL(ArrayAVLMerge(L1Tree, L1, R2Tree, R2))
        self.T2 = ArrayAVL(ArrayAVLMerge(L2Tree, L2, R1Tree, R1))
        del L1Tree, L2Tree, R1Tree, R2Tree



def ArrayAVLMerge(tree1, R1, tree2, R2):
    """Merges two ArrayAVL trees, tree1 and tree2, with roots R1 and R2, using the largest element in R1's tree as the node for merging, into a new ArrayAVL tree.
    CONSTRAINTS: All keys in R1's tree must be smaller than all keys in tree rooted at R2.
    INPUTS are two trees (tree1 and tree2) and their roots (R1 and R2): tree1, R1, tree2, R2.
    OUTPUT (the return value of this function) is root of the new tree, with all the elements of both trees.
    USAGE: Since this function actually returns a node, and not a tree, we should create an ArrayAVL tree rooted at the return value of this function. Then, we can delete tree1 and tree2 to free memory up.
    """
    if not R1:
        return R2
    if not R2:
        return R1
    T = tree1.find(float("inf"), R1)
    T.setHeight(1)
    R1 = tree1.AVLDelete(T)                                                 # we have to update R1, in case it was the largest key in tree1 when it got deleted - in case we are deleting the root
    if T == R1:                                                             # this means that T is the only node in tree1, i.e., tree1 has only that one node, which we don't delete, but we're not going to duplicate it now, either
        tree2.AVLInsert(R1.getKey(), R1.getColor(), R2)
        return R2
    root = AVL.AVLMergeWithRoot(tree1, R1, tree2, R2, T)
    return root

def _AVLSplitRec(tree, R, x):
    """
    Splits AVL tree into two trees.
    Input: An AVL tree; its root R; key x.
    Output: Roots of two AVL trees, one with elements <= x, the other with elements > x.
    Usage: User should set parents of both trees' roots to None after creating the two trees rooted at those two roots, and this should be done in two separate try-except blocks,
    because a tree might be empty. Usage example: "try: tree1/2.getRoot().setParent(None) except: pass". Of course, this can alternatively be achieved by using two "if" clauses.
    Also, user can delete node with key x from the left tree (tree1) after creating the trees, and AFTER fixing the parents, in case they want to remove x from the first tree as well,
    so that they have only elements < x, and not <= x ( tree1.AVLDelete(tree1.find(x, tree1.getRoot())) ).
    """
    if not R:
        return (None, None)
    if x < R.getKey():
        R1, R2 = _AVLSplitRec(tree, R.getLeftChild(), x)
        R3 = AVL.AVLMergeWithRoot(tree, R2, tree, R.getRightChild(), R)
        return R1, R3
    if x >= R.getKey():
        R1, R2 = _AVLSplitRec(tree, R.getRightChild(), x)
        R3 = AVL.AVLMergeWithRoot(tree, R.getLeftChild(), tree, R1, R)
        return R3, R2

def ArrayAVLSplit(tree, R, x):
    """
    Splits AVL tree into two trees.
    Input: An AVL tree; its root R; key x.
    Output: Roots of two AVL trees, one with elements <= x, the other with elements > x.
    Usage: User can delete node with key x from the left tree (tree1) after creating the trees, in case they want to remove x from the first tree as well,
    so that they have only elements < x, and not <= x ( tree1.AVLDelete(tree1.find(x, tree1.getRoot())) ).
    Also, user can delete the original tree to save memory.
    """
    if x == R.getKey():
        right = R.getRightChild()
        R.setRightChild(None)
        if right:
            right.setParent(None)
        rightHeight = 0
        left = R.getLeftChild()
        leftHeight = left.getHeight() if left else 0
        if leftHeight > rightHeight + 2:
            tree.AVLDelete(R)
            tree.AVLInsert(R.getKey(), R.getColor(), tree.getRoot())
            tree.rebalance(tree.getRoot())
        else:
            tree.rebalance(R)
        return tree.getRoot(), right

    elif R.getLeftChild() == tree.find(x, R):
        left = R.getLeftChild()
        leftsRight = left.getRightChild()
        left.setParent(None)
        if leftsRight:
            left.setRightChild(None)
            leftsRight.setParent(R)
            R.setLeftChild(leftsRight)
            leftHeight = leftsRight.getHeight()
        else:
            R.setLeftChild(None)
            leftHeight = 0
        leftTree = ArrayAVL(left)
        leftTree.rebalance(left)
        leftRoot = leftTree.getRoot()
        del leftTree
        right = R.getRightChild()
        rightHeight = right.getHeight() if right else 0
        if rightHeight > leftHeight + 2:
            tree.AVLDelete(R)
            tree.AVLInsert(R.getKey(), R.getColor(), tree.getRoot())
            tree.rebalance(tree.getRoot())
        else:
            tree.rebalance(R)
        return leftRoot, tree.getRoot()

    elif tree.previous(R) == tree.find(x, R):
        prev = tree.previous(R)
        prevParent = prev.getParent()
        while prevParent != R:
            prevParent = prevParent.getParent()
        if prevParent == R:
            prevParent = R.getLeftChild()
        prevParent.setParent(None)
        prevsRight = prev.getRightChild()
        if prevsRight:
            prev.setRightChild(None)
            prevsRight.setParent(R)
            R.setLeftChild(prevsRight)
            leftHeight = prevsRight.getHeight()
        else:
            R.setLeftChild(None)
            leftHeight = 0
        leftTree = ArrayAVL(prevParent)
        leftTree.rebalance(prevParent)
        leftRoot = leftTree.getRoot()
        leftTree.getRoot().setParent(None)
        del leftTree
        right = R.getRightChild()
        rightHeight = right.getHeight() if right else 0
        if rightHeight > leftHeight + 2:
            tree.AVLDelete(R)
            tree.AVLInsert(R.getKey(), R.getColor(), tree.getRoot())
            tree.rebalance(tree.getRoot())
        else:
            tree.rebalance(R)
        return leftRoot, tree.getRoot()

    else:
        R1, R2 = _AVLSplitRec(tree, R, x)
        if R1:
            R1.setParent(None)
        if R2:
            R2.setParent(None)
        return R1, R2




if __name__ == "__main__":
    array = Array(7)
    print(array)
    array.setColor(4, 'b')
    array.toggle(5)
    array.push('b')
    array.push('w')
    array.push('w')
    print(array)
    array.pop()
    print(array)

    print()
    for i in range(1, array.getSize() + 1):
        print(array)
        array.flip(i)
        print(array)
        array.flip(i)
        print()

    print()
    for i in range(1, array.getSize() + 1):
        print(array.getElement(i))

    print()
    k = 6
    print("Color of the {}. element: {}.".format(k, array.getColor(k)))
    print("The {}. element: {}.".format(k, array.getElement(k)))
