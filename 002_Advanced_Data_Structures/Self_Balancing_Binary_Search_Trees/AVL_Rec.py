"""
Recursive version
This version assumes that keys of all nodes in a tree are different, that they don't repeat.
This also helps:
https://en.wikipedia.org/wiki/AVL_tree
https://en.wikipedia.org/wiki/Tree_rotation
http://www.cs.usfca.edu/~galles/visualization/AVLtree.html

I'm not sure that the split() function is totally correct.
"""

import BST_Rec as BST
from Node import Node

class AVLNode(Node):

    def __init__(self, key, height = 1):
        """key is an integer value.
        New nodes are always added as leaves, thus default height of 1.
        """
        assert key != None and height != None, "Node must be added with both key and height!"
        self.height = height
        return super(AVLNode, self).__init__(key)

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def printNode(self):
        print("Key: {}, Parent: {}, Left child: {}, Right child: {}, Size: {}, Height: {}".format(self.key, self.parent, self.left, self.right, self.size, self.height))

    def __repr__(self):
        """This can be used as:
           print(repr(avl.find(key, root)))
           But, it's also very useful for debugging, because debugger will show us the (key, height) of the node without the need for expanding the node.
        """
        return "Key: {}, Size: {}, Height: {}".format(self.key, self.size, self.height)


class AVLTree(BST.BinarySearchTree):

    def __init__(self, root):
        """Expects a root node object as input."""
        return super(AVLTree, self).__init__(root)

    def __str__(self):
        return "Root = {}".format(repr(self.root))

    def __repr__(self):
        """Useful for debugging.
        The first part returns the original value of __repr__(), which contains type of the object and its address in memory.
        The second part gives us information about the root of the tree, which are its key and height, because it calls its __repr__() method.
        It's enough to just call __repr__() of the super class.
        """
        return super(AVLTree, self).__repr__()

    def height(self, node):
        """Input: node object
           This method calculates height of the node.
           Doesn't expect that node heights have been properly set in advance.
           This method will recursively calculate the node's height, but it will not set height of any node.
        """
        if node == None:
            return 0
        try:
            return 1 + max(self.height(node.getLeftChild()), self.height(node.getRightChild()))
        except ValueError:
            return 1

    def height(self, node):
        """Input: node object
           This method calculates height of the node.
           Expects that node heights have been properly set in advance!
           But, AVLInsert() method does that for us.
           But, this version will work a lot faster, because it only reads heights of the left and right child and adds 1 to the larger one.
           This version doesn't depend on recursion.
           It will not set height of any node.
           It could, though, right before return - it could call "node.setHeight(1 + max(leftHeight, rightHeight))", and then return the same value.
           But, the way the rest of the code works, that's not needed to be done here. Height will be adjusted in other places.
        """
        if node == None:
            return None
        left, right = node.getLeftChild(), node.getRightChild()
        if left:
            leftHeight = left.getHeight()
        else:
            leftHeight = 0
        if right:
            rightHeight = right.getHeight()
        else:
            rightHeight = 0
        return 1 + max(leftHeight, rightHeight)

    def insert(self, key, root):
        """Inputs: key is a numerical value; root is the root node object.
           Adds AVL node with key key and height 1 to the tree (new nodes are always added as leaves, thus height 1).
           Returns nothing.
           Node is always inserted as a leaf, so its size is 1.
           I had to override method insert() from BinarySearchTree() class because it creates a Node object, where method adjustHeight()
           expects AVLNode object when calling setHeight() on the node.
           Of course, I could just copy the whole body of this method to AVLInsert(), instead of overriding insert(), but it looks more clear this way.
        """
        parent = self.find(key, root)
        node = AVLNode(key)
        node.setParent(parent)
        if key < parent.getKey():
            parent.setLeftChild(node)
        else:
            parent.setRightChild(node)
        while parent:
            parent.incrementSize()
            parent = parent.getParent()

    def AVLInsert(self, key, root):
        """Inputs: key is a numerical value; root is the root node object.
           Adds AVL node with key key to the tree. Returns nothing.
        """
        self.insert(key, root)
        node = self.find(key, root)
        self.rebalance(node)

    def rebalance(self, node):
        """
        If a subtree of the node is too heavy, it should be lifted (promoted) up, by the means of rotation.
        This algorithm for rebalancing the AVL tree is based on the claim that heights of the two subtrees never differ by more than 2.
        """
        parent = node.getParent()
        left, right = node.getLeftChild(), node.getRightChild()
        if left:
            leftHeight = self.height(left)
        else:
            leftHeight = 0
        if right:
            rightHeight = self.height(right)
        else:
            rightHeight = 0
        if leftHeight > rightHeight + 1:                                    # If the left subtree of the node is too heavy, it should be lifted (promoted) up, by the means of right rotation.
            self.rebalanceRight(node)
        if rightHeight > leftHeight + 1:                                    # If the right subtree of the node is too heavy, it should be lifted (promoted) up, by the means of left rotation.
            self.rebalanceLeft(node)
        self.adjustHeight(node)
        self.recomputeSize(node)
        if parent:
            self.rebalance(parent)

    def adjustHeight(self, node):
        if node:
            h = self.height(node)
            node.setHeight(h)

    def rebalanceRight(self, node):
        parent = node.getParent()
        M = node.getLeftChild()
        if M:
            X = M.getRightChild()
        else:
            X = None
        if M and X and M.getLeftChild() and (self.height(X) > self.height(M.getLeftChild())):    # If the inner subtree of M, X, is higher than the other child of M (left), we first have to lift (promote) X up by rotating M left.
            self.rotateLeft(M)
            self.adjustHeight(M)
            self.adjustHeight(X)
            self.adjustHeight(node)
        self.rotateRight(node)
        self.adjustHeight(node)
        self.adjustHeight(M)
        self.adjustHeight(X)
        while parent:
            self.adjustHeight(parent)
            parent = parent.getParent()
        return self.root

    def rebalanceLeft(self, node):
        parent = node.getParent()
        M = node.getRightChild()
        if M:
            X = M.getLeftChild()                                            # M.left (C.left)
        else:
            X = None
        if M and X and M.getRightChild() and (self.height(X) > self.height(M.getRightChild())):   # If the inner subtree of M, X, is higher than the other child of M (right), we first have to lift (promote) X up by rotating M right.
            self.rotateRight(M)
            self.adjustHeight(M)
            self.adjustHeight(X)
            self.adjustHeight(node)
        self.rotateLeft(node)
        self.adjustHeight(node)
        self.adjustHeight(M)
        self.adjustHeight(X)
        while parent:
            self.adjustHeight(parent)
            parent = parent.getParent()
        return self.root

    def rotateRight(self, node):
        """Input: A node object that we want to rotate right.
           Returns the tree's root object.
           This is the same method like in class BinarySearchTree from BST_Rec module.
           I just reordered some operations, to be like at https://en.wikipedia.org/wiki/AVL_tree, but there's no real difference.
           Both methods work the same in the end.
           I'm not adjusting heights in this method, unlike Wikipedia. I do that in the three rebalance methods.
           Wikipedia also returns new root of the rotated subtree, where I return the tree's root.
        """
        parent = node.getParent()
        Y = node.getLeftChild()
        if not Y:
            return self.root                                                # we can't rotate the node with nothing!
        B = Y.getRightChild()
        node.setLeftChild(B)
        if B:
            B.setParent(node)
        Y.setRightChild(node)
        node.setParent(Y)
        Y.setParent(parent)
        if parent:
            if node.getKey() < parent.getKey():                             # node is left child
                parent.setLeftChild(Y)
            elif node.getKey() > parent.getKey():                           # node is right child
                parent.setRightChild(Y)
        else:
            self.root = Y
        self.recomputeSize(node)
        self.recomputeSize(Y)
        return self.root

    def rotateLeft(self, node):
        """Input: A node object that we want to rotate left.
           Returns the tree's root object.
           This is the same method like in class BinarySearchTree from BST_Rec module.
           I just reordered some operations, to be like at https://en.wikipedia.org/wiki/AVL_tree, but there's no real difference.
           Both methods work the same in the end.
           I'm not adjusting heights in this method, unlike Wikipedia. I do that in the three rebalance methods.
           Wikipedia also returns new root of the rotated subtree, where I return the tree's root.
        """
        # we're just rotating back now, to the left
        parent = node.getParent()
        X = node.getRightChild()
        if not X:
            return self.root                                                # we can't rotate the node with nothing!
        B = X.getLeftChild()
        node.setRightChild(B)
        if B:
            B.setParent(node)
        X.setLeftChild(node)
        node.setParent(X)
        X.setParent(parent)
        if parent:
            if node.getKey() < parent.getKey():                             # node is left child
                parent.setLeftChild(X)
            elif node.getKey() > parent.getKey():                           # node is right child
                parent.setRightChild(X)
        else:
            self.root = X
        self.recomputeSize(node)
        self.recomputeSize(X)
        return self.root

    def AVLDelete(self, node):
        """Input: node object
           Removes the node from the tree.
           Returns the tree's root object.
        """
        key = node.getKey()
        root = self.delete(node)
        M = self.find(key, root)
        self.rebalance(M)
        return self.root

    def AVLDelete(self, node):
        """Input: node object
           Removes the node from the tree.
           Returns the tree's root object.
        """
        parent = node.getParent()
        right = node.getRightChild()
        X = self.next(node)                                                 # the node that replaces "node"
        if X:
            if X != right:
                M = X.getParent()                                           # parent of node replacing "node"
                if not M:
                    M = X
            else:
                M = X
        else:
            M = self.previous(node)
        root = self.delete(node)
        if M:                                                               # this check is needed only because of the case where 'node' is the only node in the tree
            self.rebalance(M)
        return self.root

    def AVLDelete(self, node):
        """Input: node object
           Removes the node from the tree.
           Returns the tree's root object.
        """
        parent = node.getParent()
        left = node.getLeftChild()
        right = node.getRightChild()

        if not right:                                                       # node doesn't have right child
            if not left and not parent:                                     # "node" is the only node in the tree
                return self.root                                            # we could set self.root to be None, but we would have a problem with printing (traversing) it, unless we changed the traversing methods - so, this leaves it in the tree
            if left:
                left.setParent(parent)
                M = left
            else:
                M = self.next(node)
                if not M:
                    M = parent
            if parent:
                if node.getKey() < parent.getKey():                         # node is left child
                    parent.setLeftChild(left)
                elif node.getKey() > parent.getKey():                       # node is right child
                    parent.setRightChild(left)
            else:                                                           # We're deleting the root.
                self.root = left                                            # Left becomes the new root.

        else:                                                               # node has right child
            X = self.next(node)                                             # meaning, X doesn't have left child
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
                M = pX
                while pX != X:
                    pX.decrementSize()
                    pX = pX.getParent()
            else:
                M = X

            if left:
                X.setLeftChild(left)
                left.setParent(X)

            X.setParent(parent)
            if parent:                                                      # We're not deleting the root.
                if node.getKey() < parent.getKey():                         # node is left child
                    parent.setLeftChild(X)
                elif node.getKey() > parent.getKey():                       # node is right child
                    parent.setRightChild(X)
            else:                                                           # We're deleting the root.
                self.root = X                                               # X becomes new root.

            self.recomputeSize(X)

        while parent:
            parent.decrementSize()
            parent = parent.getParent()

        self.rebalance(M)

        node.setParent(None)
        node.setLeftChild(None)
        node.setRightChild(None)
        del node
        return self.root



def AVLMergeWithRoot(tree1, R1, tree2, R2, T):
    """Merges two AVL trees, tree1 and tree2, with roots R1 and R2, using an extra node T, into a new AVL tree.
    It's very possible that T will not end up as root of the new tree, because we are merging two AVL trees, and the final tree also has to be balanced.
    CONSTRAINTS: All keys in R1's tree must be smaller than all keys in tree rooted at R2. Also, T's key has to be greater than all keys in R1's tree, and less than all the keys in R2's tree.
    INPUTS are two trees (tree1 and tree2), their roots (R1 and R2), and the node T: tree1, R1, tree2, R2, T.
    OUTPUT (the return value of this function) is root of the new tree, with all the elements of both trees, and including node T.
    USAGE: Since this function actually returns a node, and not a tree, we should create an AVL tree rooted at the return value of this function. Then, we can delete tree1 and tree2 to free memory up.
    """
    assert T, "T must be != None"
    if R1:
        assert R1.getKey() < T.getKey(), "R1 has to be < T"
        R1Height = R1.getHeight()
    else:
        R1Height = 0
    if R2:
        assert T.getKey() < R2.getKey(), "T has to be < R2"
        R2Height = R2.getHeight()
    else:
        R2Height = 0
    if -1 <= R1Height - R2Height <= 1:
        T.setLeftChild(R1)
        T.setRightChild(R2)
        if R1:
            R1.setParent(T)
        if R2:
            R2.setParent(T)
        T.setHeight(max(R1Height, R2Height) + 1)
        T.recomputeSize()
        return T
    elif R1Height > R2Height:
        Rprime = AVLMergeWithRoot(tree1, R1.getRightChild(), tree2, R2, T)
        if R1 == Rprime:
            tree1.rebalance(R1)
            return tree1.getRoot()
        R1.setRightChild(Rprime)
        Rprime.setParent(R1)

        if R1.getParent() == Rprime:
            R1.setParent(None)
            tree1.setRoot(R1)

        tree1.rebalance(R1)
        return tree1.getRoot()
    elif R1Height < R2Height:
        Rprime = AVLMergeWithRoot(tree1, R1, tree2, R2.getLeftChild(), T)
        if R2 == Rprime:
            tree2.rebalance(R2)
            return tree2.getRoot()
        R2.setLeftChild(Rprime)
        Rprime.setParent(R2)

        if R2.getParent() == Rprime:
            R2.setParent(None)
            tree2.setRoot(R2)

        tree2.rebalance(R2)
        return tree2.getRoot()

def AVLMerge(tree1, R1, tree2, R2):
    """Merges two AVL trees, tree1 and tree2, with roots R1 and R2, using the largest element in R1's tree as the node for merging, into a new AVL tree.
    It's very possible that the element will not end up as root of the new tree, because we are merging two AVL trees, and the final tree also has to be balanced.
    CONSTRAINTS: All keys in R1's tree must be smaller than all keys in tree rooted at R2.
    INPUTS are two trees (tree1 and tree2) and their roots (R1 and R2): tree1, R1, tree2, R2.
    OUTPUT (the return value of this function) is root of the new tree, with all the elements of both trees.
    USAGE: Since this function actually returns a node, and not a tree, we should create an AVL tree rooted at the return value of this function. Then, we can delete tree1 and tree2 to free memory up.
    """
    if not R1:
        return R2
    if not R2:
        return R1
    T = tree1.find(float("inf"), R1)
    T.setHeight(1)
    R1 = tree1.AVLDelete(T)                                                 # we have to update R1, in case it was the largest key in tree1 when it got deleted - in case we are deleting the root
    if T == R1:                                                             # this means that T is the only node in tree1, i.e., tree1 has only that one node, which we don't delete, but we're not going to duplicate it now, either
        tree2.AVLInsert(R1.getKey(), R2)
        return R2
    root = AVLMergeWithRoot(tree1, R1, tree2, R2, T)
    return root

def _AVLSplitRec(tree, R, x):
    """
    ?!Not quite correct?!
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
        R3 = AVLMergeWithRoot(tree, R2, tree, R.getRightChild(), R)
        return R1, R3
    if x >= R.getKey():
        R1, R2 = _AVLSplitRec(tree, R.getRightChild(), x)
        R3 = AVLMergeWithRoot(tree, R.getLeftChild(), tree, R1, R)
        return R3, R2

def AVLSplit(tree, R, x):
    """
    Splits AVL tree into two trees.
    Input: An AVL tree; its root R; key x.
    Output: Roots of two AVL trees, one with elements <= x, the other with elements > x.
    Usage: User can delete node with key x from the left tree (tree1) after creating the trees, in case they want to remove x from the first tree as well,
    so that they have only elements < x, and not <= x ( tree1.AVLDelete(tree1.find(x, tree1.getRoot())) ).
    Also, user can delete the original tree to save memory.
    """
    if x == R.getKey():                                                     # if we're splitting at root
        right = R.getRightChild()
        R.setRightChild(None)
        if right:
            right.setParent(None)
        rightHeight = 0
        left = R.getLeftChild()
        leftHeight = left.getHeight() if left else 0
        if leftHeight > rightHeight + 2:
            tree.AVLDelete(R)
            tree.AVLInsert(R.getKey(), tree.getRoot())
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
        leftTree = AVLTree(left)
        leftTree.rebalance(left)
        leftRoot = leftTree.getRoot()
        del leftTree
        right = R.getRightChild()
        rightHeight = right.getHeight() if right else 0
        if rightHeight > leftHeight + 2:
            tree.AVLDelete(R)
            tree.AVLInsert(R.getKey(), tree.getRoot())
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
        leftTree = AVLTree(prevParent)
        leftTree.rebalance(prevParent)
        leftRoot = leftTree.getRoot()
        leftTree.getRoot().setParent(None)
        del leftTree
        right = R.getRightChild()
        rightHeight = right.getHeight() if right else 0
        if rightHeight > leftHeight + 2:
            tree.AVLDelete(R)
            tree.AVLInsert(R.getKey(), tree.getRoot())
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

def AVLSplitLess(tree, R, x):
    """
    Splits AVL tree into two trees.
    Input: An AVL tree; its root R; key x.
    Output: Roots of two AVL trees, one with elements < x (thus "Less" in the name), the other with elements >= x.
    Usage: User can delete node with key x from the right tree (tree2) after creating the trees, in case they want to remove x from the second tree as well,
    so that they have only elements > x, and not >= x ( tree2.AVLDelete(tree2.find(x, tree2.getRoot())) ).
    Also, user can delete the original tree to save memory.
    """
    x -= 1
    return AVLSplit(tree, R, x)

def _AVLSplitLessRec(tree, R, x):
    """
    Splits AVL tree into two trees.
    Input: An AVL tree; its root R; key x.
    Output: Roots of two AVL trees, one with elements < x (thus "Less" in the name), the other with elements >= x.
    Usage: User should set parents of both trees' roots to None after creating the two trees rooted at those two roots, and this should be done in two separate try-except blocks,
    because a tree might be empty. Usage example: "try: tree1/2.getRoot().setParent(None) except: pass". Of course, this can alternatively be achieved by using two "if" clauses.
    Also, user can delete node with key x from the right tree (tree2) after creating the trees, and AFTER fixing the parents, in case they want to remove x from the second tree as well,
    so that they have only elements > x, and not >= x ( tree2.AVLDelete(tree2.find(x, tree2.getRoot())) ).
    """
    if not R:
        return (None, None)
    if x <= R.getKey():
        R1, R2 = _AVLSplitLessRec(tree, R.getLeftChild(), x)
        R3 = AVLMergeWithRoot(tree, R2, tree, R.getRightChild(), R)
        return R1, R3
    if x > R.getKey():
        R1, R2 = _AVLSplitLessRec(tree, R.getRightChild(), x)
        R3 = AVLMergeWithRoot(tree, R.getLeftChild(), tree, R1, R)
        return R3, R2

def AVLSplitLess(tree, R, x):
    """
    Splits AVL tree into two trees.
    Input: An AVL tree; its root R; key x.
    Output: Roots of two AVL trees, one with elements < x (thus "Less" in the name), the other with elements >= x.
    Usage: User can delete node with key x from the right tree (tree2) after creating the trees, in case they want to remove x from the second tree as well,
    so that they have only elements > x, and not >= x ( tree2.AVLDelete(tree2.find(x, tree2.getRoot())) ).
    Also, user can delete the original tree to save memory.
    """
    if x == R.getKey():
        left = R.getLeftChild()
        R.setLeftChild(None)
        if left:
            left.setParent(None)
        leftHeight = 0
        right = R.getRightChild()
        rightHeight = right.getHeight() if right else 0
        if rightHeight > leftHeight + 2:
            tree.AVLDelete(R)
            tree.AVLInsert(R.getKey(), tree.getRoot())
            tree.rebalance(tree.getRoot())
        else:
            tree.rebalance(R)
        return left, tree.getRoot()

    elif R.getRightChild() == tree.find(x, R):
        right = R.getRightChild()
        if x > right.getKey():
            return R, None
        rightsLeft = right.getLeftChild()
        right.setParent(None)
        if rightsLeft:
            right.setLeftChild(None)
            rightsLeft.setParent(R)
            R.setRightChild(rightsLeft)
            rightHeight = rightsLeft.getHeight()
        else:
            R.setRightChild(None)
            rightHeight = 0
        rightTree = AVLTree(right)
        rightTree.rebalance(right)
        rightRoot = rightTree.getRoot()
        del rightTree
        left = R.getLeftChild()
        leftHeight = left.getHeight() if left else 0
        if leftHeight > rightHeight + 2:
            tree.AVLDelete(R)
            tree.AVLInsert(R.getKey(), tree.getRoot())
            tree.rebalance(tree.getRoot())
        else:
            tree.rebalance(R)
        return tree.getRoot(), rightRoot

    elif tree.next(R) == tree.find(x, R):
        next = tree.next(R)
        nextParent = next.getParent()
        while nextParent != R:
            nextParent = nextParent.getParent()
        if nextParent == R:
            nextParent = R.getRightChild()
        nextParent.setParent(None)
        nextsLeft = next.getLeftChild()
        if nextsLeft:
            next.setLeftChild(None)
            nextsLeft.setParent(R)
            R.setRightChild(nextsLeft)
            rightHeight = nextsLeft.getHeight()
        else:
            R.setRightChild(None)
            rightHeight = 0
        rightTree = AVLTree(nextParent)
        rightTree.rebalance(nextParent)
        rightRoot = rightTree.getRoot()
        rightTree.getRoot().setParent(None)
        del rightTree
        left = R.getLeftChild()
        leftHeight = left.getHeight() if left else 0
        if leftHeight > rightHeight + 2:
            tree.AVLDelete(R)
            tree.AVLInsert(R.getKey(), tree.getRoot())
            tree.rebalance(tree.getRoot())
        else:
            tree.rebalance(R)
        return tree.getRoot(), rightRoot

    else:
        R1, R2 = _AVLSplitLessRec(tree, R, x)
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


def printAVLTree(avl, verbose = False):
    """If boolean verbose is True, it will print(all nodes, in BFS order.
       We can safely assign avl.getRoot() to root variable here, and work with it every time, because this function doesn't modify the tree;
       it only reads it, and prints it in-order, pre-order, and breadth first, and it also prints heights of all nodes in-order.
       But, in other cases, we should be careful, and it's better to use avl.getRoot() every time. It's probably slower, but safer, and more elegant.
       Methods like AVLInsert(), or AVLDelete(), modify the AVL tree, and can also change the root node, because of balancing operations (which include rotations).
    """
    root = avl.getRoot()
    print()
    print("In order:  ", avl.inOrder(root))
    print("Pre order: ", avl.preOrder(root))
    print("BFS:       ", avl.BFS(root))
    print("Heights (in order):")
    nodes = avl.inOrder(root)
    for node in nodes:
        print(node, avl.height(avl.find(node, root)))
    if verbose:
        print("Nodes (in BFS order):")
        nodes = avl.BFS(root)
        for node in nodes:
            avl.find(node, root).printNode()
    print()
