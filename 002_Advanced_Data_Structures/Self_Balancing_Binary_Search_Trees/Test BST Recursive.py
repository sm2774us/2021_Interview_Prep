"""
Recursive version
This version assumes that keys of all nodes in a tree are different, that they don't repeat.
Uncomment desired test calls.
"""

import BST_Rec as BST


def printTree(bst, verbose = False):
    """Works nicely, and is elegant, but can be optimized for speed."""
    print()
    print("In order:  ", bst.inOrder(bst.getRoot()))
    print("Pre order: ", bst.preOrder(bst.getRoot()))
    print("BFS:       ", bst.BFS(bst.getRoot()))
    if verbose:
        print("Nodes (in BFS order):")
        nodes = bst.BFS(bst.getRoot())
        for node in nodes:
            bst.find(node, bst.getRoot()).printNode()
    print()


def printTree(bst, verbose = False):
    """If boolean verbose is True, it will print(all nodes, in BFS order.
       This is optimized version of the above function.
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


def createTree():
    """We can do it like this..."""
    n1 = BST.Node(1)
    n4 = BST.Node(4)
    n6 = BST.Node(6)
    n7 = BST.Node(7)                                    # root
    n10 = BST.Node(10)
    n13 = BST.Node(13)
    n15 = BST.Node(15)

    n1.setParent(n4)
    n6.setParent(n4)
    n4.setParent(n7)
    n10.setParent(n13)
    n15.setParent(n13)
    n13.setParent(n7)

    n4.setLeftChild(n1)
    n4.setRightChild(n6)
    n7.setLeftChild(n4)
    n7.setRightChild(n13)
    n13.setLeftChild(n10)
    n13.setRightChild(n15)

    bst = BST.BinarySearchTree(n7)
    root = n7

    return bst, root


def createTree():
    """...But it's definitely better this way!"""

    # We must create the root node first!
    n7 = BST.Node(7)                                    # root

    # Then we create the BST tree with that root node.
    root = n7
    bst = BST.BinarySearchTree(root)

    # Only now can we add other nodes; we couldn't before creating the BST tree! We must use insert() method!
    bst.insert(4, root)
    bst.insert(1, root)
    bst.insert(6, root)
    bst.insert(13, root)
    bst.insert(15, root)
    bst.insert(10, root)

    return bst, root


def createTree():
    """...And probably the best this way!"""

    # We must create the root node first!
    # Then we create the BST tree with that root node.
    bst = BST.BinarySearchTree(BST.Node(7))

    # Only now can we add other nodes; we couldn't before creating the BST tree! We must use insert() method!
    bst.insert(4, bst.getRoot())
    bst.insert(1, bst.getRoot())
    bst.insert(6, bst.getRoot())
    bst.insert(13, bst.getRoot())
    bst.insert(15, bst.getRoot())
    bst.insert(10, bst.getRoot())

    return bst, bst.getRoot()


def testTree():
    bst, root = createTree()

    print("\nPrint:")
    print("In order Rec:    ", bst.inOrderR(root))
    print("In order Iter:   ", bst.inOrder(root))
    print("Pre order Iter:  ", bst.preOrder(root))
    print("Post order Rec:  ", bst.postOrderR(root))
    print("Post order Iter: ", bst.postOrder(root))
    print("Level order Iter:", bst.BFS(root))
    print("Root:", end=' ')
    root.printNode()

    print("\nprint(left subtree:")
    print("In order Rec:    ", bst.inOrderR(root.getLeftChild()))
    print("In order Iter:   ", bst.inOrder(root.getLeftChild()))
    print("Pre order Iter:  ", bst.preOrder(root.getLeftChild()))
    print("Post order Rec:  ", bst.postOrderR(root.getLeftChild()))
    print("Post order Iter: ", bst.postOrder(root.getLeftChild()))
    print("Level order Iter:", bst.BFS(root.getLeftChild()))
    print("Root of the left subtree:", end=' ')
    root.getLeftChild().printNode()

    printTree(bst, True)

    print("\nFind:")
    print(0, bst.find(0, root))
    print(1, bst.find(1, root))
    print(2, bst.find(2, root))
    print(5, bst.find(5, root))
    print(6, bst.find(6, root))
    print(7, bst.find(7, root))
    print(8, bst.find(8, root))
    print(12, bst.find(12, root))
    print(13, bst.find(13, root))
    print(14, bst.find(14, root))
    print(15, bst.find(15, root))
    print(20, bst.find(20, root))

    print("\nFind first: {}".format(bst.findMin(root)))
    print("\nFind last: {}".format(bst.findMax(root)))

    print("\nFind subtree minimum:")
    print(7, bst.subtreeMinimum(root))
    print(4, bst.subtreeMinimum(bst.find(4, root)))
    print(1, bst.subtreeMinimum(bst.find(1, root)))
    print(6, bst.subtreeMinimum(bst.find(6, root)))
    print(13, bst.subtreeMinimum(bst.find(13, root)))
    print(10, bst.subtreeMinimum(bst.find(10, root)))
    print(15, bst.subtreeMinimum(bst.find(15, root)))
    print(None, bst.subtreeMinimum(None))

    print("\nFind subtree maximum:")
    print(7, bst.subtreeMaximum(root))
    print(4, bst.subtreeMaximum(bst.find(4, root)))
    print(1, bst.subtreeMaximum(bst.find(1, root)))
    print(6, bst.subtreeMaximum(bst.find(6, root)))
    print(13, bst.subtreeMaximum(bst.find(13, root)))
    print(10, bst.subtreeMaximum(bst.find(10, root)))
    print(15, bst.subtreeMaximum(bst.find(15, root)))
    print(None, bst.subtreeMaximum(None))

    print("\nNext:")
    print(0, bst.next(bst.find(0, root)))
    print(1, bst.next(bst.find(1, root)))
    print(2, bst.next(bst.find(2, root)))
    print(4, bst.next(bst.find(4, root)))
    print(5, bst.next(bst.find(5, root)))
    print(6, bst.next(bst.find(6, root)))
    print(7, bst.next(bst.find(7, root)))
    print(8, bst.next(bst.find(8, root)))
    print(10, bst.next(bst.find(10, root)))
    print(12, bst.next(bst.find(12, root)))
    print(14, bst.next(bst.find(14, root)))
    print(15, bst.next(bst.find(15, root)))
    print(16, bst.next(bst.find(16, root)))

    print("\nPrevious:")
    print(0, bst.previous(bst.find(0, root)))
    print(1, bst.previous(bst.find(1, root)))
    print(2, bst.previous(bst.find(2, root)))
    print(4, bst.previous(bst.find(4, root)))
    print(5, bst.previous(bst.find(5, root)))
    print(6, bst.previous(bst.find(6, root)))
    print(7, bst.previous(bst.find(7, root)))
    print(8, bst.previous(bst.find(8, root)))
    print(10, bst.previous(bst.find(10, root)))
    print(12, bst.previous(bst.find(12, root)))
    print(14, bst.previous(bst.find(14, root)))
    print(15, bst.previous(bst.find(15, root)))
    print(16, bst.previous(bst.find(16, root)))

    print("\nRange search:")
    print(5, 12)
    for node in bst.rangeSearch(5, 12, root):
        print(node, end=' ')
    print()

    if 0:                                               # put 1 to execute this
        print("\nInsert:")
        print("In order:  ", bst.inOrder(root))
        print("Pre order: ", bst.preOrder(root))
        print("BFS:       ", bst.BFS(root))
        n = 3                                           # key of the node to insert
        bst.insert(n, root)
        node = bst.find(n, root)
        node.printNode()
        node.getParent().printNode()
        print("Inserting", n)
        print("In order:  ", bst.inOrder(root))
        print("Pre order: ", bst.preOrder(root))
        print("BFS:       ", bst.BFS(root))

        print()
        print("In order:  ", bst.inOrder(root))
        print("Pre order: ", bst.preOrder(root))
        print("Post order:", bst.postOrder(root))
        print("BFS:       ", bst.BFS(root))
        n = 5                                           # key of the node to insert
        bst.insert(n, root)
        node = bst.find(n, root)
        node.printNode()
        node.getParent().printNode()
        print("Inserting", n)
        print("In order:  ", bst.inOrder(root))
        print("Pre order: ", bst.preOrder(root))
        print("Post order:", bst.postOrder(root))
        print("BFS:       ", bst.BFS(root))

    if 0:                                               # put 1 to execute this
        print("\nDelete:")
        printTree(bst, True)
        n = 7                                           # key of the node to delete (make sure to try with the root node!)
        root = bst.delete(bst.find(n, root))            # We must not forget to reassign the root, because of the case when we're deleting the root node!!!
        print("Deleting", n)
        printTree(bst, True)
        print("This is the node under which the deleted node, {}, would come: {}.".format(n, bst.find(n, root)))
        bst.find(n, root).printNode()
        try:
            bst.find(n, root).getParent().printNode()
        except:
            print("New root:", end=' ')
            bst.find(root.getKey(), root).printNode()
        print("Root is:", end=' ')
        bst.getRoot().printNode()

    if 0:                                               # put 1 to execute this
        print("\nDelete Key:")
        printTree(bst, True)
        n = 7                                           # key of the node to delete (make sure to try with the root node!)
        r = bst.deleteKey(n)                            # We must not forget to reassign the root, because of the case when we're deleting the root node!!!
        if r:                                           # If key n was found in the tree, then it got deleted, and we have to assign r to root. If key n wasn't found, deleteKey() returns None, and we don't change the root.
            root = r
        print("Deleting", n)
        if r:
            print("{} found and deleted.".format(n))
        else:
            print("{} not found. Nothing was deleted.".format(n))
        printTree(bst, True)
        print("This is the node under which the deleted node, {}, would come: {}.".format(n, bst.find(n, root)))
        bst.find(n, root).printNode()
        try:
            bst.find(n, root).getParent().printNode()
        except:
            print("New root:", end=' ')
            bst.find(root.getKey(), root).printNode()
        print("Root is:", end=' ')
        bst.getRoot().printNode()

    print("\nRotate right:")
    print("In order:  ", bst.inOrder(root))
    print("Pre order: ", bst.preOrder(root))
    print("BFS:       ", bst.BFS(root))
    n = 4                                               # key of the node to rotate (make sure to try with the root node!)
    root = bst.rotateRight(bst.find(n, root))           # We must not forget to reassign the root, because of the case when we're rotating the root node!!!
    print("Rotating right", n)
    printTree(bst, True)

    print("\nRotate left:")
    print("In order:  ", bst.inOrder(root))
    print("Pre order: ", bst.preOrder(root))
    print("BFS:       ", bst.BFS(root))
    n = 7                                               # key of the node to rotate (make sure to try with the root node!)
    root = bst.rotateLeft(bst.find(n, root))            # We must not forget to reassign the root, because of the case when we're rotating the root node!!!
    print("Rotating left", n)
    printTree(bst, True)


def test0a():
    bst = BST.BinarySearchTree(BST.Node(10))            # root
    printTree(bst, True)
    bst.delete(bst.find(10, bst.getRoot()))
    printTree(bst, True)


def test0b():
    bst = BST.BinarySearchTree(BST.Node(10))            # root
    printTree(bst, True)
    bst.deleteKey(10)
    printTree(bst, True)


def test1():
    bst = BST.BinarySearchTree(BST.Node(3))             # root
    bst.insert(1, bst.getRoot())
    bst.insert(4, bst.getRoot())
    bst.insert(5, bst.getRoot())
    printTree(bst, True)
    bst.delete(bst.find(3, bst.getRoot()))
    printTree(bst, True)


def test2a():
    bst, root = createTree()
    #bst.insert(11, bst.getRoot())
    printTree(bst, True)
    bst.delete(bst.find(7, bst.getRoot()))
    printTree(bst, True)

def test2b():
    bst, root = createTree()
    bst.insert(11, bst.getRoot())
    bst.insert(14, bst.getRoot())
    printTree(bst, True)
    bst.deleteKey(15)
    printTree(bst, True)


def test3():
    bst = BST.BinarySearchTree(BST.Node(5))             # root
    bst.insert(1, bst.getRoot())
    printTree(bst, True)
    bst.delete(bst.find(1, bst.getRoot()))
    printTree(bst, True)
    print("Root:", bst.getRoot())



testTree()
#test0a()
#test0b()
#test1()
#test2a()
#test2b()
#test3()



def testMWR():
    bst1 = BST.BinarySearchTree(BST.Node(3))
    bst1.insert(2, bst1.getRoot())
    bst1.insert(1, bst1.getRoot())
    bst1.insert(5, bst1.getRoot())
    bst1.insert(4, bst1.getRoot())
    bst1.insert(7, bst1.getRoot())
    bst1.insert(6, bst1.getRoot())
    printTree(bst1, True)

    bst2 = BST.BinarySearchTree(BST.Node(9))
    bst2.insert(11, bst2.getRoot())
    bst2.insert(10, bst2.getRoot())
    printTree(bst2, True)

    T = BST.Node(8)

    bst = BST.mergeWithRoot(bst1, bst2, T)
    del bst1, bst2, T
    printTree(bst, True)


def testMerge1():
    bst1 = BST.BinarySearchTree(BST.Node(3))
    bst1.insert(2, bst1.getRoot())
    bst1.insert(1, bst1.getRoot())
    bst1.insert(5, bst1.getRoot())
    bst1.insert(4, bst1.getRoot())
    bst1.insert(7, bst1.getRoot())
    bst1.insert(6, bst1.getRoot())
    bst1.insert(8, bst1.getRoot())
    printTree(bst1, True)

    bst2 = BST.BinarySearchTree(BST.Node(9))
    bst2.insert(11, bst2.getRoot())
    bst2.insert(10, bst2.getRoot())
    printTree(bst2, True)

    T = BST.merge(bst1, bst2)
    printTree(T, True)


def testMerge2():
    bst1 = BST.BinarySearchTree(BST.Node(8))
    bst1.insert(2, bst1.getRoot())
    bst1.insert(1, bst1.getRoot())
    bst1.insert(5, bst1.getRoot())
    bst1.insert(4, bst1.getRoot())
    bst1.insert(7, bst1.getRoot())
    bst1.insert(6, bst1.getRoot())
    printTree(bst1, True)

    bst2 = BST.BinarySearchTree(BST.Node(9))
    bst2.insert(11, bst2.getRoot())
    bst2.insert(10, bst2.getRoot())
    printTree(bst2, True)

    T = BST.merge(bst1, bst2)
    printTree(T, True)


def testMerge3():
    bst1 = BST.BinarySearchTree(BST.Node(3))
    bst1.insert(2, bst1.getRoot())
    bst1.insert(1, bst1.getRoot())
    bst1.insert(5, bst1.getRoot())
    bst1.insert(4, bst1.getRoot())
    bst1.insert(8, bst1.getRoot())
    bst1.insert(7, bst1.getRoot())
    bst1.insert(6, bst1.getRoot())
    printTree(bst1, True)

    bst2 = BST.BinarySearchTree(BST.Node(9))
    bst2.insert(11, bst2.getRoot())
    bst2.insert(10, bst2.getRoot())
    printTree(bst2, True)

    T = BST.merge(bst1, bst2)
    printTree(T, True)

    print(T)
    print(repr(T))


def testMerge4():
    bst1 = BST.BinarySearchTree(BST.Node(1))
    printTree(bst1, True)

    bst2 = BST.BinarySearchTree(BST.Node(2))
    bst2.insert(3, bst2.getRoot())
    bst2.insert(4, bst2.getRoot())
    printTree(bst2, True)

    bst = BST.merge(bst1, bst2)
    del bst1, bst2
    printTree(bst, True)


#testMWR()
#testMerge1()
#testMerge2()
#testMerge3()
#testMerge4()


def testMWRNodes1():
    bst1 = BST.BinarySearchTree(BST.Node(3))
    bst1.insert(2, bst1.getRoot())
    bst1.insert(1, bst1.getRoot())
    bst1.insert(5, bst1.getRoot())
    bst1.insert(4, bst1.getRoot())
    bst1.insert(7, bst1.getRoot())
    bst1.insert(6, bst1.getRoot())
    printTree(bst1, True)

    bst2 = BST.BinarySearchTree(BST.Node(9))
    bst2.insert(11, bst2.getRoot())
    bst2.insert(10, bst2.getRoot())
    printTree(bst2, True)

    T = BST.Node(8)

    root = BST.mergeWithRootNodes(bst1.getRoot(), bst2.getRoot(), T)
    del bst1, bst2, T
    bst = BST.BinarySearchTree(root)
    printTree(bst, True)


def testMWRNodes2():
    bst1 = None
    try:
        printTree(bst1, True)
    except:
        print(None)

    bst2 = BST.BinarySearchTree(BST.Node(2))
    printTree(bst2, True)

    T = BST.Node(1)

    root = BST.mergeWithRootNodes(bst1, bst2.getRoot(), T)
    del bst1, bst2, T
    bst = BST.BinarySearchTree(root)
    printTree(bst, True)


def testMWRNodes3():
    bst1 = BST.BinarySearchTree(BST.Node(1))
    printTree(bst1, True)

    bst2 = None
    try:
        printTree(bst2, True)
    except:
        print(None)

    T = BST.Node(2)

    root = BST.mergeWithRootNodes(bst1.getRoot(), bst2, T)
    del bst1, bst2, T
    bst = BST.BinarySearchTree(root)
    printTree(bst, True)


def testMWRNodes4():
    bst1 = BST.BinarySearchTree(BST.Node(1))
    printTree(bst1, True)

    bst2 = BST.BinarySearchTree(BST.Node(3))
    bst2.insert(4, bst2.getRoot())
    printTree(bst2, True)

    T = BST.Node(2)

    root = BST.mergeWithRootNodes(bst1.getRoot(), bst2.getRoot(), T)
    del bst1, bst2
    bst = BST.BinarySearchTree(root)
    printTree(bst, True)



#testMWRNodes1()
#testMWRNodes2()
#testMWRNodes3()
#testMWRNodes4()



def testMergeNodes1():
    bst1 = BST.BinarySearchTree(BST.Node(3))
    bst1.insert(2, bst1.getRoot())
    bst1.insert(1, bst1.getRoot())
    bst1.insert(5, bst1.getRoot())
    bst1.insert(4, bst1.getRoot())
    bst1.insert(7, bst1.getRoot())
    bst1.insert(6, bst1.getRoot())
    bst1.insert(8, bst1.getRoot())
    printTree(bst1, True)

    bst2 = BST.BinarySearchTree(BST.Node(9))
    bst2.insert(11, bst2.getRoot())
    bst2.insert(10, bst2.getRoot())
    printTree(bst2, True)

    root = BST.mergeNodes(bst1, bst1.getRoot(), bst2, bst2.getRoot())
    del bst1, bst2
    bst = BST.BinarySearchTree(root)
    printTree(bst, True)


def testMergeNodes2():
    bst1 = BST.BinarySearchTree(BST.Node(1))
    printTree(bst1, True)

    bst2 = BST.BinarySearchTree(BST.Node(2))
    bst2.insert(3, bst2.getRoot())
    bst2.insert(4, bst2.getRoot())
    printTree(bst2, True)

    root = BST.mergeNodes(bst1, bst1.getRoot(), bst2, bst2.getRoot())
    del bst1, bst2
    bst = BST.BinarySearchTree(root)
    printTree(bst, True)


def testMergeNodes3():
    bst1 = BST.BinarySearchTree(BST.Node(2))
    bst1.insert(1, bst1.getRoot())
    printTree(bst1, True)

    bst2 = BST.BinarySearchTree(BST.Node(3))
    printTree(bst2, True)

    root = BST.mergeNodes(bst1, bst1.getRoot(), bst2, bst2.getRoot())
    del bst1, bst2
    bst = BST.BinarySearchTree(root)
    printTree(bst, True)


def testMergeNodes4():
    bst1 = BST.BinarySearchTree(BST.Node(2))
    bst1.insert(1, bst1.getRoot())
    printTree(bst1, True)

    bst2 = BST.BinarySearchTree(BST.Node(3))
    printTree(bst2, True)

    root = BST.mergeNodes(bst1, bst1.getRoot(), None, None)
    del bst1, bst2
    bst = BST.BinarySearchTree(root)
    printTree(bst, True)


#testMergeNodes1()
#testMergeNodes2()
#testMergeNodes3()
#testMergeNodes4()



def testSplit1():
    bst = BST.BinarySearchTree(BST.Node(3))
    bst.insert(2, bst.getRoot())
    bst.insert(1, bst.getRoot())
    bst.insert(6, bst.getRoot())
    printTree(bst, True)

    root1, root2 = BST.split(bst.getRoot(), 4)
    del bst
    bst1, bst2 = BST.BinarySearchTree(root1), BST.BinarySearchTree(root2)
    try:
        printTree(bst1, True)
    except:
        print("Empty tree")
    try:
        printTree(bst2, True)
    except:
        print("Empty tree")


def testSplit2():
    bst = BST.BinarySearchTree(BST.Node(3))
    bst.insert(2, bst.getRoot())
    bst.insert(1, bst.getRoot())
    bst.insert(6, bst.getRoot())
    printTree(bst, True)

    root1, root2 = BST.splitLess(bst.getRoot(), 3)
    del bst
    bst1, bst2 = BST.BinarySearchTree(root1), BST.BinarySearchTree(root2)
    try:
        printTree(bst1, True)
    except:
        print("Empty tree")
    try:
        printTree(bst2, True)
    except:
        print("Empty tree")


def testSplit3():
    bst = BST.BinarySearchTree(BST.Node(3))
    bst.insert(2, bst.getRoot())
    bst.insert(1, bst.getRoot())
    bst.insert(6, bst.getRoot())
    bst.insert(5, bst.getRoot())
    bst.insert(4, bst.getRoot())
    bst.insert(7, bst.getRoot())
    bst.insert(8, bst.getRoot())
    bst.insert(9, bst.getRoot())
    printTree(bst, True)

    x = 2
    root1, root2 = BST.split(bst.getRoot(), x)
    del bst
    bst1, bst2 = BST.BinarySearchTree(root1), BST.BinarySearchTree(root2)
    try:
        printTree(bst1, True)
    except:
        print("Empty tree")
    try:
        printTree(bst2, True)
    except:
        print("Empty tree")
    #bst1.delete(bst1.find(x, bst1.getRoot()))           # this is needed only in case we want to remove n from the first tree as well, so that we have only elements < x, and not <= x
    #printTree(bst1, True)


def testSplit4():
    bst = BST.BinarySearchTree(BST.Node(3))
    bst.insert(2, bst.getRoot())
    bst.insert(1, bst.getRoot())
    bst.insert(6, bst.getRoot())
    bst.insert(5, bst.getRoot())
    bst.insert(4, bst.getRoot())
    bst.insert(7, bst.getRoot())
    bst.insert(8, bst.getRoot())
    bst.insert(9, bst.getRoot())
    printTree(bst, True)

    x = 0
    root1, root2 = BST.splitLess(bst.getRoot(), x)
    del bst
    bst1, bst2 = BST.BinarySearchTree(root1), BST.BinarySearchTree(root2)
    try:
        #bst1.getRoot().setParent(None)
        printTree(bst1, True)
    except:
        print(None)
    try:
        #bst2.getRoot().setParent(None)
        printTree(bst2, True)
    except:
        print(None)
    #bst2.delete(bst2.find(x, bst2.getRoot()))           # this is needed only in case we want to remove n from the first tree as well, so that we have only elements < x, and not <= x
    #printTree(bst2, True)


def testSplitA():
    bst = BST.BinarySearchTree(BST.Node(2))
    bst.insert(1, bst.getRoot())
    bst.insert(3, bst.getRoot())
    bst.insert(20, bst.getRoot())
    bst.insert(10, bst.getRoot())
    bst.insert(8, bst.getRoot())
    bst.insert(9, bst.getRoot())
    bst.insert(15, bst.getRoot())
    bst.insert(14, bst.getRoot())
    bst.insert(11, bst.getRoot())
    bst.insert(12, bst.getRoot())
    bst.insert(13, bst.getRoot())
    bst.insert(16, bst.getRoot())
    bst.insert(17, bst.getRoot())
    bst.insert(18, bst.getRoot())
    bst.insert(25, bst.getRoot())
    printTree(bst, True)

    x = 24
    root1, root2 = BST.splitLess(bst.getRoot(), x)
    del bst
    bst1, bst2 = BST.BinarySearchTree(root1), BST.BinarySearchTree(root2)
    try:
        printTree(bst1, True)
    except:
        print("Empty tree")
    try:
        printTree(bst2, True)
    except:
        print("Empty tree")


def testSplitB():
    bst = BST.BinarySearchTree(BST.Node(11))
    bst.insert(6, bst.getRoot())
    bst.insert(4, bst.getRoot())
    bst.insert(2, bst.getRoot())
    bst.insert(5, bst.getRoot())
    bst.insert(7, bst.getRoot())
    bst.insert(8, bst.getRoot())
    printTree(bst, True)

    x = 0
    root1, root2 = BST.split(bst.getRoot(), x)
    del bst
    bst1, bst2 = BST.BinarySearchTree(root1), BST.BinarySearchTree(root2)
    try:
        printTree(bst1, True)
    except:
        print("Empty tree")
    try:
        printTree(bst2, True)
    except:
        print("Empty tree")


#testSplit1()
#testSplit2()
#testSplit3()
#testSplit4()
#testSplitA()
#testSplitB()



def testOrderStatistic1():
    bst = BST.BinarySearchTree(BST.Node(10))            # root
    printTree(bst, True)
    k = 1
    print("{}. element is:".format(k), end=' ')
    print(BST.orderStatistic(bst.getRoot(), k))


def testOrderStatistic2():
    bst = BST.BinarySearchTree(BST.Node(5))             # root
    bst.insert(1, bst.getRoot())
    printTree(bst, True)
    k = 2
    print("{}. element is:".format(k), end=' ')
    print(BST.orderStatistic(bst.getRoot(), k))


def testOrderStatistic3():
    bst, root = createTree()
    bst.insert(11, bst.getRoot())
    printTree(bst, True)
    k = 6
    print("{}. element is:".format(k), end=' ')
    print(BST.orderStatistic(bst.getRoot(), k))


def testOrderStatistic4():
    bst = BST.BinarySearchTree(BST.Node(3))
    bst.insert(2, bst.getRoot())
    bst.insert(1, bst.getRoot())
    bst.insert(6, bst.getRoot())
    bst.insert(5, bst.getRoot())
    bst.insert(4, bst.getRoot())
    bst.insert(7, bst.getRoot())
    bst.insert(8, bst.getRoot())
    bst.insert(9, bst.getRoot())
    printTree(bst, True)
    k = 6
    print("{}. element is:".format(k), end=' ')
    print(BST.orderStatistic(bst.getRoot(), k))


#testOrderStatistic1()
#testOrderStatistic2()
#testOrderStatistic3()
#testOrderStatistic4()


def testOrderStatisticZero():
    """Run it in pair with testOrderStatistic4()."""
    bst = BST.BinarySearchTree(BST.Node(3))
    bst.insert(2, bst.getRoot())
    bst.insert(1, bst.getRoot())
    bst.insert(6, bst.getRoot())
    bst.insert(5, bst.getRoot())
    bst.insert(4, bst.getRoot())
    bst.insert(7, bst.getRoot())
    bst.insert(8, bst.getRoot())
    bst.insert(9, bst.getRoot())
    printTree(bst, True)
    k = 5
    print("{}. element, if we count from 1, is: {}.".format(k+1, BST.orderStatisticZeroBasedRanking(bst.getRoot(), k)))
    print("But that element has index {} if we count from 0.".format(k))



#testOrderStatisticZero()



def testComputeRank():
    bst, root = createTree()
    printTree(bst, True)
    for key in range(19):
        print("Rank of element with the key {} is:".format(key), end=' ')
        print(BST.computeRank(bst.getRoot(), bst, key))
        print()


#testComputeRank()