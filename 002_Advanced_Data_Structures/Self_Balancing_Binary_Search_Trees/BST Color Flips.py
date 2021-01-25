"""
This is an application of Binary Search Trees.
It's used for storing an array in a tree (or two trees), and it was invented to speed things up.
Uses 1-based indexing.
Non-balancing BST, which we use here, has O(n) time complexity in the worst case, like a regular array (list).
We should use a balancing BST instead. An example with AVL trees is included in this project.
"""

import BST_Rec as BST


class ArrayNode(BST.Node):

    def __init__(self, key, color):
        assert key != None and (color == 'b' or color == 'w'), "Node must be added with both key and color ('b' or 'w')!"
        self.color = color
        return super(ArrayNode, self).__init__(key)

    def setColor(self, color):
        assert color == 'b' or color == 'w', "Color can be either 'b' or 'w'!"
        self.color = color

    def getColor(self):
        return self.color

    def printNode(self):
        print("Key: {}, Parent: {}, Left child: {}, Right child: {}, Size: {}, Color: {}".format(self.key, self.parent, self.left, self.right, self.size, repr(self.color)))

    def __str__(self):
        return str((self.key, self.color))

    def __repr__(self):
        """This can be used as:
           print(repr(tree.find(key, root)))
           But, it's also very useful for debugging, because debugger will show us the key of the node without the need for expanding the node.
           Of course, we can add some other pieces of information, too.
           We can return "str(self.key)" and concatenate other string to it, or we can use the form below. Anyhow, we must return a string.
        """
        return "Key: {}, Size: {}, Color: {}".format(self.key, self.size, repr(self.color))


class ArrayBST(BST.BinarySearchTree):

    def __init__(self, root):
        """Expects a root node object as input."""
        return super(ArrayBST, self).__init__(root)

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
           Adds ArrayNode with key key and color color to the ArrayBST tree.
           Returns nothing.
           Node is always inserted as a leaf, so its size is 1.
           I had to override method insert() from BinarySearchTree() class because it creates a Node object which doesn't contain the color field.
        """
        parent = self.find(key, root)
        node = ArrayNode(key, color)
        node.setParent(parent)
        if key < parent.getKey():
            parent.setLeftChild(node)
        else:
            parent.setRightChild(node)
        while parent:
            parent.incrementSize()
            parent = parent.getParent()


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
        self.T1.insert(self.size, color, self.T1.getRoot())
        self.T2.insert(self.size, self.oppositeColor(color), self.T2.getRoot())

    def pop(self):
        """
        Pops an element from the end of the array and returns it.
        """
        el1 = self.T1.find(self.size, self.T1.getRoot())
        self.T1.delete(el1)
        el2 = self.T2.find(self.size, self.T2.getRoot())
        self.T2.delete(el2)
        self.decrementSize()
        return el1

    def newArray(self, n):
        """
        Creates two ArrayBST trees, T1 and T2, with keys [1, n].
        All nodes in T1 have color 'w' (white), and all nodes in T2 have color 'b' (black).
        Returns T1, T2.
        """
        T1 = ArrayBST(ArrayNode(1, 'w'))
        for i in range(2, n + 1):
            T1.insert(i, 'w', T1.getRoot())

        T2 = ArrayBST(ArrayNode(1, 'b'))
        for i in range(2, n + 1):
            T2.insert(i, 'b', T2.getRoot())

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
        L1, R1 = BST.split(self.T1.getRoot(), x)
        L2, R2 = BST.split(self.T2.getRoot(), x)
        L1Tree = ArrayBST(L1)
        L2Tree = ArrayBST(L2)
        R1Tree = ArrayBST(R1)
        R2Tree = ArrayBST(R2)
        self.T1 = ArrayBST(ArrayMergeNodes(L1Tree, L1, R2Tree, R2))
        self.T2 = ArrayBST(ArrayMergeNodes(L2Tree, L2, R1Tree, R1))
        del L1Tree, L2Tree, R1Tree, R2Tree



def ArrayMergeNodes(tree1, R1, tree2, R2):
    """Merges two ArrayBST trees, tree1 and tree2, with roots R1 and R2, using the largest element in R1's tree as root of the new ArrayBST tree.
    Constraints: All keys in R1's tree must be smaller than all keys in tree rooted at R2.
    Inputs are two trees (tree1 and tree2) and their roots (R1 and R2): tree1, R1, tree2, R2.
    Output is root of the new tree, T, with all the elements of both trees.
    Usage: Since this function actually returns a node, and not a tree, we should create an ArrayBST tree rooted at the return value of this function. Then, we can delete tree1 and tree2 to free memory up.
    """
    if not R1:
        return R2
    if not R2:
        return R1
    T = tree1.find(float("inf"), R1)
    R1 = tree1.delete(T)                                        # we have to update R1, in case it was the largest key in tree1 when it got deleted - in case we are deleting the root
    if T == R1:                                                 # this means that T is the only node in tree1, i.e., tree1 has only that one node, which we don't delete, but we're not going to duplicate it now, either
        tree2.insert(R1.getKey(), R1.getColor(), R2)
        return R2
    BST.mergeWithRootNodes(R1, R2, T)
    return T



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
