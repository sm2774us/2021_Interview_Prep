"""
Recursive version
This version assumes that keys of all nodes in a tree are different, that they don't repeat.
This also helps: http://www.cs.usfca.edu/~galles/visualization/AVLtree.html
Uncomment desired test calls.
"""

import AVL_Rec as AVL


def printAVLTree(avl, verbose = False):
    """Works nicely, and is elegant, but can be optimized for speed."""
    print()
    print("In order:  ", avl.inOrder(avl.getRoot()))
    print("Pre order: ", avl.preOrder(avl.getRoot()))
    print("BFS:       ", avl.BFS(avl.getRoot()))
    print("Heights (in order):")
    nodes = avl.inOrder(avl.getRoot())
    for node in nodes:
        print(node, avl.height(avl.find(node, avl.getRoot())))
    if verbose:
        print("Nodes (in BFS order):")
        nodes = avl.BFS(avl.getRoot())
        for node in nodes:
            avl.find(node, avl.getRoot()).printNode()
    print()


def printAVLTree(avl, verbose = False):
    """If boolean verbose is True, it will print(all nodes, in BFS order.
       This is optimized version of the above function.
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


def testAVLshort():
    """This is the proper way of creating an AVL tree."""

    # We must create a root node first! The root might change later, when we insert new nodes!
    n1 = AVL.AVLNode(1)

    # Then we create the AVL tree with that root node.
    avl = AVL.AVLTree(n1)
    printAVLTree(avl, True)

    # Only now can we add other nodes; we couldn't before creating the AVL tree! We must use AVLInsert() method!
    # By using avl.getRoot(), we don't have to think in which places we have to reassign root manually every time.
    # By the way, we would have to do that right after every AVLInsert operation, or during AVLDelete, because it returns the tree's root.
    avl.AVLInsert(4, avl.getRoot())
    printAVLTree(avl, True)
    avl.AVLInsert(6, avl.getRoot())
    printAVLTree(avl, True)
    avl.AVLInsert(7, avl.getRoot())
    printAVLTree(avl, True)
    avl.AVLInsert(13, avl.getRoot())
    printAVLTree(avl, True)
    avl.AVLInsert(15, avl.getRoot())
    printAVLTree(avl, True)
    avl.AVLInsert(10, avl.getRoot())
    printAVLTree(avl, True)


def createTree():
    """This is the proper way of creating an AVL tree."""

    # We must create a root node first! The root might change later, when we insert new nodes!
    n7 = AVL.AVLNode(7)

    # Then we create the AVL tree with that root node.
    avl = AVL.AVLTree(n7)

    # Only now can we add other nodes; we couldn't before creating the AVL tree! We must use AVLInsert() method!
    # By using avl.getRoot(), we don't have to think in which places we have to reassign root manually every time.
    # By the way, we would have to do that right after every AVLInsert operation, or during AVLDelete, because it returns the tree's root.
    avl.AVLInsert(1, avl.getRoot())
    avl.AVLInsert(4, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    avl.AVLInsert(13, avl.getRoot())
    avl.AVLInsert(15, avl.getRoot())
    avl.AVLInsert(10, avl.getRoot())

    return avl, avl.getRoot()


def testAVLTree():
    """This is the proper way of working with an AVL tree."""
    avl, root = createTree()

    print("\nPrint:")
    print("In order:  ", avl.inOrder(root))
    print("Pre order: ", avl.preOrder(root))
    print("Post order:", avl.postOrder(root))
    print("BFS:       ", avl.BFS(root))
    print("Root:", end=' ')
    root.printNode()

    # Or...

    # This probably calculates avl.getRoot() every time it's called, but it's more elegant, and looks more like iterative version.
    print("\nPrint:")
    print("In order:  ", avl.inOrder(avl.getRoot()))
    print("Pre order: ", avl.preOrder(avl.getRoot()))
    print("Post order:", avl.postOrder(avl.getRoot()))
    print("BFS:       ", avl.BFS(avl.getRoot()))
    print("Root:", end=' ')
    avl.getRoot().printNode()

    print()
    print(repr(root))
    print(repr(avl.find(4, root)))

    print("\nHeight:")
    print(1, avl.height(avl.find(1, root)))
    print(4, avl.height(avl.find(4, root)))
    print(6, avl.height(avl.find(6, root)))
    print(root, root.getHeight(), avl.height(root))
    print(10, avl.height(avl.find(10, root)))
    print(13, avl.height(avl.find(13, root)))
    print(15, avl.height(avl.find(15, root)))

    # Or...

    printAVLTree(avl, True)

    if 0:                                               # put 1 to execute this
        print("\nRebalance right:")
        avl.insert(2, root)                             # This plain insert() can't change the root node, so we don't have to reassign the root (with "root = avl.getRoot()").
        avl.insert(3, root)                             # This plain insert() can't change the root node, so we don't have to reassign the root (with "root = avl.getRoot()").
        avl.find(3, root).setHeight(1)                  # I have to manually set heights of these five nodes because I use avl.insert(), and not avl.AVLInsert()!
        avl.find(2, root).setHeight(2)
        avl.find(1, root).setHeight(3)
        avl.find(4, root).setHeight(4)
        avl.find(7, root).setHeight(5)
        printAVLTree(avl, True)
        print(root, root.getHeight(), avl.height(root))
        n = 4                                           # key of the node to rebalance right
        root = avl.rebalanceRight(avl.find(n, root))    # We must not forget to reassign the root, because of the case when we're rebalancing (rotating) the root node!!! But, I shouldn't use rebalanceRight() here anyway!
        print("Rebalancing right", n)
        printAVLTree(avl, True)
        print(root, root.getHeight(), avl.height(root))
        avl.find(n, root).printNode()

    if 0:                                               # put 1 to execute this
        print("\nRebalance left:")
        avl.find(13, root).key = 12                     # I need node 13 to be 12. This won't change the root node, so we don't have to reassign the root (with "root = avl.getRoot()").
        avl.insert(14, root)                            # This plain insert() can't change the root node, so we don't have to reassign the root (with "root = avl.getRoot()").
        avl.insert(13, root)                            # This plain insert() can't change the root node, so we don't have to reassign the root (with "root = avl.getRoot()").
        avl.find(13, root).setHeight(1)                 # I have to manually set heights of these five nodes because I use avl.insert(), and not avl.AVLInsert()!
        avl.find(14, root).setHeight(2)
        avl.find(15, root).setHeight(3)
        avl.find(12, root).setHeight(4)
        avl.find(7, root).setHeight(5)
        printAVLTree(avl, True)
        print(root, root.getHeight(), avl.height(root))
        n = 12                                          # key of the node to rebalance left
        root = avl.rebalanceLeft(avl.find(n, root))     # We must not forget to reassign the root, because of the case when we're rebalancing (rotating) the root node!!! But, I shouldn't use rebalanceLeft() here anyway!
        print("Rebalancing left", n)
        printAVLTree(avl, True)
        print(root, root.getHeight(), avl.height(root))
        avl.find(n, root).printNode()

    if 0:                                               # put 1 to execute this
        print("\n*** AVL Insert: ***\n")
        printAVLTree(avl, True)
        n = 2                                           # key of the node to insert
        avl.AVLInsert(n, root)
        root = avl.getRoot()                            # We must not forget to reassign the root right after the AVLInsert operation! This is because we use "root" instead of "avl.getRoot()" in all our method calls.
        node = avl.find(n, root)
        print("Inserting", n)
        node.printNode()
        node.getParent().printNode()
        printAVLTree(avl, True)

        n = 3                                           # key of the node to insert
        avl.AVLInsert(n, root)
        root = avl.getRoot()                            # We must not forget to reassign the root right after the AVLInsert operation! This is because we use "root" instead of "avl.getRoot()" in all our method calls.
        node = avl.find(n, root)
        print("Inserting", n)
        node.printNode()
        node.getParent().printNode()
        printAVLTree(avl, True)

    if 0:                                               # put 1 to execute this
        print("\n*** AVL Insert: ***\n")
        avl.find(13, root).key = 12                     # I need node 13 to be 12. This won't change the root node, so we don't have to reassign the root (with "root = avl.getRoot()").
        printAVLTree(avl, True)
        n = 14                                          # key of the node to insert
        avl.AVLInsert(n, root)
        root = avl.getRoot()                            # We must not forget to reassign the root right after the AVLInsert operation! This is because we use "root" instead of "avl.getRoot()" in all our method calls.
        node = avl.find(n, root)
        print("Inserting", n)
        node.printNode()
        node.getParent().printNode()
        printAVLTree(avl, True)

        n = 13                                          # key of the node to insert
        avl.AVLInsert(n, root)
        root = avl.getRoot()                            # We must not forget to reassign the root right after the AVLInsert operation! This is because we use "root" instead of "avl.getRoot()" in all our method calls.
        node = avl.find(n, root)
        print("Inserting", n)
        node.printNode()
        node.getParent().printNode()
        printAVLTree(avl, True)

    if 1:                                               # put 1 to execute this
        print("\n*** AVL Delete: ***\n")
        avl.AVLInsert(0, root)
        avl.AVLInsert(11, root)
        avl.AVLInsert(16, root)
        root = avl.getRoot()                            # We must not forget to reassign the root right after the AVLInsert operation! This is because we use "root" instead of "avl.getRoot()" in all our method calls.
        printAVLTree(avl, True)
        print(root, root.getHeight(), avl.height(root))
        n = 7                                           # key of the node to delete (make sure to try with the root node!)
        root = avl.AVLDelete(avl.find(n, root))         # We must not forget to reassign the root during the AVLDelete operation!
        print("Deleting", n)
        print("This is the node under which the deleted node, {}, would come: {}.".format(n, avl.find(n, root)))
        avl.find(n, root).printNode()
        try:
            avl.find(n, root).getParent().printNode()
        except:
            print("New root:", end=' ')
            avl.find(root.getKey(), root).printNode()
        print("Root is:", end=' ')
        avl.getRoot().printNode()
        printAVLTree(avl, True)
        print(root, root.getHeight(), avl.height(root))

    if 0:                                               # put 1 to execute this
        # Same as above, only we use avl.getRoot() here, which is nicer, because we don't have to manually reassign root when needed. We also insert the deleted node at the end.
        # We should do it like this always, when we use operations that modify the tree, like AVLInsert and AVLDelete.
        # It's not necessary for finding or printing, where it can be sped up by using root and not calculating avl.getRoot() every time.
        print("\n*** AVL Delete: ***\n")
        avl.AVLInsert(0, avl.getRoot())
        printAVLTree(avl, True)
        print(avl.getRoot(), avl.getRoot().getHeight(), avl.height(avl.getRoot()))
        n = 4                                           # key of the node to delete (make sure to try with the root node!)
        avl.AVLDelete(avl.find(n, avl.getRoot()))       # Now we don't have to reassign the root during the AVLDelete operation!
        print("Deleting", n)
        print("This is the node under which the deleted node, {}, would come: {}.".format(n, avl.find(n, avl.getRoot())))
        avl.find(n, avl.getRoot()).printNode()
        try:
            avl.find(n, avl.getRoot()).getParent().printNode()
        except:
            print("New root:", end=' ')
            avl.find(avl.getRoot().getKey(), avl.getRoot()).printNode()
        print("Root is:", end=' ')
        avl.getRoot().printNode()
        printAVLTree(avl, True)
        print(avl.getRoot(), avl.getRoot().getHeight(), avl.height(avl.getRoot()))
        print("Inserting", n)
        avl.AVLInsert(n, avl.getRoot())
        printAVLTree(avl, True)
        print(avl.getRoot(), avl.getRoot().getHeight(), avl.height(avl.getRoot()))


def readInsert(avl):
    key = None
    while True:
        try:
            key = int(input("Input key to insert: "))
        except ValueError:
            if key == 'd' or 'D':
                readDelete(avl)
            elif key == 'q' or 'Q':
                return
            else:
                return
        avl.AVLInsert(key, avl.getRoot())
        printAVLTree(avl, True)

def readDelete(avl):
    key = None
    while True:
        try:
            key = int(input("Input key to delete: "))
        except ValueError:
            if key == 'i' or 'I':
                readInsert(avl)
            elif key == 'q' or 'Q':
                return
            else:
                return
        avl.AVLDelete(avl.find(key, avl.getRoot()))
        printAVLTree(avl, True)

def testInteractive():
    key = int(input("Input the first key: "))
    avl = AVL.AVLTree(AVL.AVLNode(key))
    readInsert(avl)


def test0():
    avl = AVL.AVLTree(AVL.AVLNode(10))
    printAVLTree(avl, True)
    avl.AVLDelete(avl.find(10, avl.getRoot()))
    printAVLTree(avl, True)


def test1():
    avl = AVL.AVLTree(AVL.AVLNode(1))
    avl.AVLInsert(3, avl.getRoot())
    avl.AVLInsert(4, avl.getRoot())
    avl.AVLInsert(5, avl.getRoot())
    printAVLTree(avl, True)
    avl.AVLDelete(avl.find(3, avl.getRoot()))
    printAVLTree(avl, True)


def test2():
    avl = AVL.AVLTree(AVL.AVLNode(4))
    avl.AVLInsert(3, avl.getRoot())
    avl.AVLInsert(5, avl.getRoot())
    avl.AVLInsert(1, avl.getRoot())
    printAVLTree(avl, True)
    avl.AVLDelete(avl.find(3, avl.getRoot()))
    #avl.AVLDelete(avl.find(4, avl.getRoot()))
    printAVLTree(avl, True)


def test3():
    avl = AVL.AVLTree(AVL.AVLNode(4))
    avl.AVLInsert(3, avl.getRoot())
    avl.AVLInsert(5, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    printAVLTree(avl, True)
    avl.AVLDelete(avl.find(6, avl.getRoot()))
    printAVLTree(avl, True)


def test4():
    avl, root = createTree()
    printAVLTree(avl, True)
    avl.AVLDelete(avl.find(7, avl.getRoot()))
    printAVLTree(avl, True)


def test5():
    avl = AVL.AVLTree(AVL.AVLNode(1))
    avl.AVLInsert(4, avl.getRoot())
    avl.AVLInsert(10, avl.getRoot())
    avl.AVLInsert(11, avl.getRoot())
    avl.AVLInsert(8, avl.getRoot())
    avl.AVLInsert(9, avl.getRoot())
    printAVLTree(avl, True)

    avl.AVLDelete(avl.find(8, avl.getRoot()))
    printAVLTree(avl, True)
    avl.AVLDelete(avl.find(1, avl.getRoot()))
    printAVLTree(avl, True)
    avl.AVLDelete(avl.find(4, avl.getRoot()))
    printAVLTree(avl, True)
    avl.AVLDelete(avl.find(10, avl.getRoot()))
    printAVLTree(avl, True)
    avl.AVLDelete(avl.find(11, avl.getRoot()))
    printAVLTree(avl, True)
    avl.AVLDelete(avl.find(9, avl.getRoot()))
    printAVLTree(avl, True)




#testAVLshort()
#testAVLTree()
#testInteractive()
#test1()
#test2()
#test3()
#test4()
#test5()



def testAVLMWR1():
    avl1 = AVL.AVLTree(AVL.AVLNode(7))
    avl1.AVLInsert(3, avl1.getRoot())
    avl1.AVLInsert(13, avl1.getRoot())
    avl1.AVLInsert(1, avl1.getRoot())
    avl1.AVLInsert(5, avl1.getRoot())
    avl1.AVLInsert(10, avl1.getRoot())
    avl1.AVLInsert(15, avl1.getRoot())
    avl1.AVLInsert(4, avl1.getRoot())
    avl1.AVLInsert(6, avl1.getRoot())
    printAVLTree(avl1, True)

    avl2 = AVL.AVLTree(AVL.AVLNode(18))
    avl2.AVLInsert(20, avl2.getRoot())
    avl2.AVLInsert(22, avl2.getRoot())
    printAVLTree(avl2, True)

    T = AVL.AVLNode(17)

    root = AVL.AVLMergeWithRoot(avl1, avl1.getRoot(), avl2, avl2.getRoot(), T)
    del avl1, avl2, T
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)


def testAVLMWR2():
    avl1 = AVL.AVLTree(AVL.AVLNode(1))
    avl1.AVLInsert(2, avl1.getRoot())
    avl1.AVLInsert(3, avl1.getRoot())
    printAVLTree(avl1, True)

    avl2 = AVL.AVLTree(AVL.AVLNode(12))
    avl2.AVLInsert(8, avl2.getRoot())
    avl2.AVLInsert(14, avl2.getRoot())
    avl2.AVLInsert(7, avl2.getRoot())
    avl2.AVLInsert(10, avl2.getRoot())
    avl2.AVLInsert(13, avl2.getRoot())
    avl2.AVLInsert(15, avl2.getRoot())
    avl2.AVLInsert(9, avl2.getRoot())
    avl2.AVLInsert(11, avl2.getRoot())
    printAVLTree(avl2, True)

    T = AVL.AVLNode(5)

    root = AVL.AVLMergeWithRoot(avl1, avl1.getRoot(), avl2, avl2.getRoot(), T)
    del avl1, avl2, T
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)

    print(avl)
    print(repr(avl))


def testAVLMWR3():
    avl1 = None
    try:
        printAVLTree(avl1, True)
    except:
        print(None)

    avl2 = AVL.AVLTree(AVL.AVLNode(2))
    printAVLTree(avl2, True)

    T = AVL.AVLNode(1)

    root = AVL.AVLMergeWithRoot(avl1, None, avl2, avl2.getRoot(), T)
    del avl1, avl2, T
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)


def testAVLMWR4():
    avl1 = AVL.AVLTree(AVL.AVLNode(3))
    avl1.AVLInsert(2, avl1.getRoot())
    avl1.AVLInsert(1, avl1.getRoot())
    printAVLTree(avl1, True)

    avl2 = None
    try:
        printAVLTree(avl2, True)
    except:
        print(None)

    T = AVL.AVLNode(6)

    root = AVL.AVLMergeWithRoot(avl1, avl1.getRoot(), avl2, None, T)
    del avl1, avl2, T
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)


def testAVLMWR5():
    avl1 = None
    try:
        printAVLTree(avl1, True)
    except:
        print(None)

    avl2 = None
    try:
        printAVLTree(avl2, True)
    except:
        print(None)

    T = AVL.AVLNode(6)

    root = AVL.AVLMergeWithRoot(avl1, None, avl2, None, T)
    del avl1, avl2, T
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)


def testAVLMWR6():
    avl1 = AVL.AVLTree(AVL.AVLNode(3))
    printAVLTree(avl1, True)

    avl2 = None
    try:
        printAVLTree(avl2, True)
    except:
        print(None)

    T = AVL.AVLNode(6)

    root = AVL.AVLMergeWithRoot(avl1, avl1.getRoot(), avl2, None, T)
    del avl1, avl2, T
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)


def testAVLMWR7():
    avl1 = AVL.AVLTree(AVL.AVLNode(3))
    printAVLTree(avl1, True)

    avl2 = AVL.AVLTree(AVL.AVLNode(8))
    printAVLTree(avl2, True)

    T = AVL.AVLNode(6)

    root = AVL.AVLMergeWithRoot(avl1, avl1.getRoot(), avl2, avl2.getRoot(), T)
    del avl1, avl2, T
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)



#testAVLMWR1()
#testAVLMWR2()
#testAVLMWR3()
#testAVLMWR4()
#testAVLMWR5()
#testAVLMWR6()
#testAVLMWR7()




def testAVLMerge0a():
    avl1 = None
    try:
        printAVLTree(avl1, True)
    except:
        print(None)

    avl2 = AVL.AVLTree(AVL.AVLNode(12))
    avl2.AVLInsert(8, avl2.getRoot())
    avl2.AVLInsert(14, avl2.getRoot())
    avl2.AVLInsert(7, avl2.getRoot())
    avl2.AVLInsert(10, avl2.getRoot())
    avl2.AVLInsert(13, avl2.getRoot())
    avl2.AVLInsert(15, avl2.getRoot())
    avl2.AVLInsert(9, avl2.getRoot())
    avl2.AVLInsert(11, avl2.getRoot())
    printAVLTree(avl2, True)

    root = AVL.AVLMerge(avl1, None, avl2, avl2.getRoot())
    del avl1, avl2
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)


def testAVLMerge0b():
    avl1 = AVL.AVLTree(AVL.AVLNode(2))
    printAVLTree(avl1, True)

    avl2 = None
    try:
        printAVLTree(avl2, True)
    except:
        print(None)

    root = AVL.AVLMerge(avl1, avl1.getRoot(), avl2, None)
    del avl1, avl2
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)


def testAVLMerge0c():
    """This shouldn't work and it doesn't."""
    avl1 = None
    try:
        printAVLTree(avl1, True)
    except:
        print(None)

    avl2 = None
    try:
        printAVLTree(avl2, True)
    except:
        print(None)

    root = AVL.AVLMerge(avl1, None, avl2, None)
    del avl1, avl2
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)


def testAVLMerge0d():
    avl1 = AVL.AVLTree(AVL.AVLNode(1))
    printAVLTree(avl1, True)

    avl2 = AVL.AVLTree(AVL.AVLNode(2))
    printAVLTree(avl2, True)

    root = AVL.AVLMerge(avl1, avl1.getRoot(), avl2, avl2.getRoot())
    del avl1, avl2
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)


def testAVLMerge1():
    avl1 = AVL.AVLTree(AVL.AVLNode(7))
    avl1.AVLInsert(3, avl1.getRoot())
    avl1.AVLInsert(13, avl1.getRoot())
    avl1.AVLInsert(1, avl1.getRoot())
    avl1.AVLInsert(5, avl1.getRoot())
    avl1.AVLInsert(10, avl1.getRoot())
    avl1.AVLInsert(15, avl1.getRoot())
    avl1.AVLInsert(17, avl1.getRoot())
    avl1.AVLInsert(4, avl1.getRoot())
    avl1.AVLInsert(6, avl1.getRoot())
    #avl1.AVLInsert(11, avl1.getRoot())
    printAVLTree(avl1, True)

    avl2 = AVL.AVLTree(AVL.AVLNode(18))
    avl2.AVLInsert(20, avl2.getRoot())
    avl2.AVLInsert(22, avl2.getRoot())
    printAVLTree(avl2, True)

    root = AVL.AVLMerge(avl1, avl1.getRoot(), avl2, avl2.getRoot())
    del avl1, avl2
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)


def testAVLMerge2():
    avl1 = AVL.AVLTree(AVL.AVLNode(2))
    avl1.AVLInsert(1, avl1.getRoot())
    avl1.AVLInsert(3, avl1.getRoot())
    avl1.AVLInsert(5, avl1.getRoot())
    printAVLTree(avl1, True)

    avl2 = AVL.AVLTree(AVL.AVLNode(12))
    avl2.AVLInsert(8, avl2.getRoot())
    avl2.AVLInsert(14, avl2.getRoot())
    avl2.AVLInsert(7, avl2.getRoot())
    avl2.AVLInsert(10, avl2.getRoot())
    avl2.AVLInsert(13, avl2.getRoot())
    avl2.AVLInsert(15, avl2.getRoot())
    avl2.AVLInsert(9, avl2.getRoot())
    avl2.AVLInsert(11, avl2.getRoot())
    printAVLTree(avl2, True)

    root = AVL.AVLMerge(avl1, avl1.getRoot(), avl2, avl2.getRoot())
    del avl1, avl2
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)

    print(avl)
    print(repr(avl))


def testAVLMerge3():
    avl1 = AVL.AVLTree(AVL.AVLNode(7))
    avl1.AVLInsert(3, avl1.getRoot())
    avl1.AVLInsert(13, avl1.getRoot())
    avl1.AVLInsert(1, avl1.getRoot())
    avl1.AVLInsert(5, avl1.getRoot())
    avl1.AVLInsert(10, avl1.getRoot())
    avl1.AVLInsert(15, avl1.getRoot())
    avl1.AVLInsert(9, avl1.getRoot())
    avl1.AVLInsert(11, avl1.getRoot())
    printAVLTree(avl1, True)

    avl2 = AVL.AVLTree(AVL.AVLNode(18))
    avl2.AVLInsert(16, avl2.getRoot())
    avl2.AVLInsert(22, avl2.getRoot())
    printAVLTree(avl2, True)

    root = AVL.AVLMerge(avl1, avl1.getRoot(), avl2, avl2.getRoot())
    del avl1, avl2
    avl = AVL.AVLTree(root)
    printAVLTree(avl, True)


#testAVLMerge0a()
#testAVLMerge0b()
#testAVLMerge0c()                                       # This shouldn't work and it doesn't.
#testAVLMerge0d()
#testAVLMerge1()
#testAVLMerge2()
#testAVLMerge3()



def testSplit1():
    avl = AVL.AVLTree(AVL.AVLNode(3))
    avl.AVLInsert(2, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    avl.AVLInsert(1, avl.getRoot())
    printAVLTree(avl, True)

    root1, root2 = AVL.AVLSplit(avl, avl.getRoot(), 5)
    del avl
    avl1, avl2 = AVL.AVLTree(root1), AVL.AVLTree(root2)
    try:
        printAVLTree(avl1, True)
    except:
        print("Empty tree")
    try:
        printAVLTree(avl2, True)
    except:
        print("Empty tree")


def testSplit2():
    avl = AVL.AVLTree(AVL.AVLNode(3))
    avl.AVLInsert(2, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    avl.AVLInsert(1, avl.getRoot())
    printAVLTree(avl, True)

    root1, root2 = AVL.AVLSplitLess(avl, avl.getRoot(), 4)
    del avl
    avl1, avl2 = AVL.AVLTree(root1), AVL.AVLTree(root2)
    try:
        printAVLTree(avl1, True)
    except:
        print("Empty tree")
    try:
        printAVLTree(avl2, True)
    except:
        print("Empty tree")


def testSplit3():
    avl = AVL.AVLTree(AVL.AVLNode(3))
    avl.AVLInsert(2, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    avl.AVLInsert(1, avl.getRoot())
    avl.AVLInsert(5, avl.getRoot())
    avl.AVLInsert(7, avl.getRoot())
    avl.AVLInsert(4, avl.getRoot())
    avl.AVLInsert(8, avl.getRoot())
    avl.AVLInsert(9, avl.getRoot())
    printAVLTree(avl, True)

    x = 2
    root1, root2 = AVL.AVLSplit(avl, avl.getRoot(), x)
    del avl
    avl1, avl2 = AVL.AVLTree(root1), AVL.AVLTree(root2)
    try:
        printAVLTree(avl1, True)
    except:
        print("Empty tree")
    try:
        printAVLTree(avl2, True)
    except:
        print("Empty tree")
    #avl1.AVLDelete(avl1.find(x, avl1.getRoot()))        # this is needed only in case we want to remove n from the first tree as well, so that we have only elements < x, and not <= x
    #printAVLTree(avl1, True)


def testSplit4():
    avl = AVL.AVLTree(AVL.AVLNode(3))
    avl.AVLInsert(2, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    avl.AVLInsert(1, avl.getRoot())
    avl.AVLInsert(5, avl.getRoot())
    avl.AVLInsert(7, avl.getRoot())
    avl.AVLInsert(4, avl.getRoot())
    avl.AVLInsert(8, avl.getRoot())
    avl.AVLInsert(9, avl.getRoot())
    printAVLTree(avl, True)

    x = -1
    root1, root2 = AVL.AVLSplitLess(avl, avl.getRoot(), x)
    del avl
    avl1, avl2 = AVL.AVLTree(root1), AVL.AVLTree(root2)
    try:
        #avl1.getRoot().setParent(None)
        printAVLTree(avl1, True)
    except:
        print("Empty tree")
    try:
        #avl2.getRoot().setParent(None)
        printAVLTree(avl2, True)
    except:
        print("Empty tree")
    #avl1.AVLDelete(avl1.find(x, avl1.getRoot()))        # this is needed only in case we want to remove n from the first tree as well, so that we have only elements < x, and not <= x
    #printAVLTree(avl1, True)


def testSplit5():
    avl = AVL.AVLTree(AVL.AVLNode(7))
    avl.AVLInsert(4, avl.getRoot())
    avl.AVLInsert(8, avl.getRoot())
    avl.AVLInsert(2, avl.getRoot())
    avl.AVLInsert(5, avl.getRoot())
    avl.AVLInsert(9, avl.getRoot())
    avl.AVLInsert(1, avl.getRoot())
    avl.AVLInsert(3, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    printAVLTree(avl, True)

    x = 4
    root1, root2 = AVL.AVLSplit(avl, avl.getRoot(), x)
    del avl
    avl1, avl2 = AVL.AVLTree(root1), AVL.AVLTree(root2)
    try:
        printAVLTree(avl1, True)
    except:
        print("Empty tree")
    try:
        printAVLTree(avl2, True)
    except:
        print("Empty tree")


def testSplit6():
    avl = AVL.AVLTree(AVL.AVLNode(7))
    avl.AVLInsert(3, avl.getRoot())
    avl.AVLInsert(9, avl.getRoot())
    avl.AVLInsert(2, avl.getRoot())
    avl.AVLInsert(4, avl.getRoot())
    avl.AVLInsert(8, avl.getRoot())
    avl.AVLInsert(10, avl.getRoot())
    avl.AVLInsert(1, avl.getRoot())
    avl.AVLInsert(11, avl.getRoot())
    #avl.AVLInsert(5, avl.getRoot())
    printAVLTree(avl, True)

    x = 4
    root1, root2 = AVL.AVLSplit(avl, avl.getRoot(), x)
    del avl
    avl1, avl2 = AVL.AVLTree(root1), AVL.AVLTree(root2)
    try:
        printAVLTree(avl1, True)
    except:
        print("Empty tree")
    try:
        printAVLTree(avl2, True)
    except:
        print("Empty tree")


def testSplit7():
    avl = AVL.AVLTree(AVL.AVLNode(4))
    avl.AVLInsert(2, avl.getRoot())
    avl.AVLInsert(7, avl.getRoot())
    avl.AVLInsert(1, avl.getRoot())
    avl.AVLInsert(3, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    avl.AVLInsert(8, avl.getRoot())
    #avl.AVLInsert(0, avl.getRoot())
    avl.AVLInsert(5, avl.getRoot())
    avl.AVLInsert(9, avl.getRoot())
    printAVLTree(avl, True)

    x = 3
    root1, root2 = AVL.AVLSplit(avl, avl.getRoot(), x)
    del avl
    avl1, avl2 = AVL.AVLTree(root1), AVL.AVLTree(root2)
    try:
        printAVLTree(avl1, True)
    except:
        print("Empty tree")
    try:
        printAVLTree(avl2, True)
    except:
        print("Empty tree")


def testSplit8():
    avl = AVL.AVLTree(AVL.AVLNode(10))
    avl.AVLInsert(5, avl.getRoot())
    avl.AVLInsert(15, avl.getRoot())
    avl.AVLInsert(3, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    avl.AVLInsert(14, avl.getRoot())
    avl.AVLInsert(16, avl.getRoot())
    avl.AVLInsert(7, avl.getRoot())
    avl.AVLInsert(13, avl.getRoot())
    avl.AVLInsert(17, avl.getRoot())
    printAVLTree(avl, True)

    x = 7
    root1, root2 = AVL.AVLSplit(avl, avl.getRoot(), x)
    del avl
    avl1, avl2 = AVL.AVLTree(root1), AVL.AVLTree(root2)
    try:
        printAVLTree(avl1, True)
    except:
        print("Empty tree")
    try:
        printAVLTree(avl2, True)
    except:
        print("Empty tree")


def testSplit9():
    avl = AVL.AVLTree(AVL.AVLNode(10))
    avl.AVLInsert(5, avl.getRoot())
    avl.AVLInsert(15, avl.getRoot())
    avl.AVLInsert(3, avl.getRoot())
    avl.AVLInsert(7, avl.getRoot())
    avl.AVLInsert(14, avl.getRoot())
    avl.AVLInsert(16, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    #avl.AVLInsert(8, avl.getRoot())
    avl.AVLInsert(13, avl.getRoot())
    avl.AVLInsert(17, avl.getRoot())
    printAVLTree(avl, True)

    x = 7
    root1, root2 = AVL.AVLSplit(avl, avl.getRoot(), x)
    del avl
    avl1, avl2 = AVL.AVLTree(root1), AVL.AVLTree(root2)
    try:
        printAVLTree(avl1, True)
    except:
        print("Empty tree")
    try:
        printAVLTree(avl2, True)
    except:
        print("Empty tree")


def testSplit10():
    avl = AVL.AVLTree(AVL.AVLNode(10))
    avl.AVLInsert(5, avl.getRoot())
    avl.AVLInsert(20, avl.getRoot())
    avl.AVLInsert(3, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    avl.AVLInsert(14, avl.getRoot())
    avl.AVLInsert(27, avl.getRoot())
    avl.AVLInsert(2, avl.getRoot())
    avl.AVLInsert(13, avl.getRoot())
    avl.AVLInsert(15, avl.getRoot())
    avl.AVLInsert(26, avl.getRoot())
    avl.AVLInsert(28, avl.getRoot())
    avl.AVLInsert(29, avl.getRoot())
    printAVLTree(avl, True)

    x = 5
    root1, root2 = AVL.AVLSplit(avl, avl.getRoot(), x)
    del avl
    avl1, avl2 = AVL.AVLTree(root1), AVL.AVLTree(root2)
    try:
        printAVLTree(avl1, True)
    except:
        print("Empty tree")
    try:
        printAVLTree(avl2, True)
    except:
        print("Empty tree")



#testSplit1()
#testSplit2()
#testSplit3()
#testSplit4()
#testSplit5()
#testSplit6()
#testSplit7()
#testSplit8()
#testSplit9()
#testSplit10()



def testOrderStatistic1():
    avl = AVL.AVLTree(AVL.AVLNode(10))                  # root
    printAVLTree(avl, True)
    k = 1
    print("{}. element is:".format(k), end=' ')
    print(AVL.orderStatistic(avl.getRoot(), k))


def testOrderStatistic2():
    avl = AVL.AVLTree(AVL.AVLNode(5))                   # root
    avl.AVLInsert(1, avl.getRoot())
    printAVLTree(avl, True)
    k = 1
    print("{}. element is:".format(k), end=' ')
    print(AVL.orderStatistic(avl.getRoot(), k))


def testOrderStatistic3():
    avl, root = createTree()
    avl.AVLInsert(11, avl.getRoot())
    printAVLTree(avl, True)
    k = 6
    print("{}. element is:".format(k), end=' ')
    print(AVL.orderStatistic(avl.getRoot(), k))


def testOrderStatistic4():
    avl = AVL.AVLTree(AVL.AVLNode(3))
    avl.AVLInsert(2, avl.getRoot())
    avl.AVLInsert(1, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    avl.AVLInsert(5, avl.getRoot())
    avl.AVLInsert(4, avl.getRoot())
    avl.AVLInsert(7, avl.getRoot())
    avl.AVLInsert(8, avl.getRoot())
    avl.AVLInsert(9, avl.getRoot())
    printAVLTree(avl, True)
    k = 6
    print("{}. element is:".format(k), end=' ')
    print(AVL.orderStatistic(avl.getRoot(), k))


#testOrderStatistic1()
#testOrderStatistic2()
#testOrderStatistic3()
#testOrderStatistic4()


def testOrderStatisticZero():
    """Run it in pair with testOrderStatistic4()."""
    avl = AVL.AVLTree(AVL.AVLNode(3))
    avl.AVLInsert(2, avl.getRoot())
    avl.AVLInsert(1, avl.getRoot())
    avl.AVLInsert(6, avl.getRoot())
    avl.AVLInsert(5, avl.getRoot())
    avl.AVLInsert(4, avl.getRoot())
    avl.AVLInsert(7, avl.getRoot())
    avl.AVLInsert(8, avl.getRoot())
    avl.AVLInsert(9, avl.getRoot())
    printAVLTree(avl, True)
    k = 5
    print("{}. element, if we count from 1, is: {}.".format(k+1, AVL.orderStatisticZeroBasedRanking(avl.getRoot(), k)))
    print("But that element has index {} if we count from 0.".format(k))


#testOrderStatisticZero()



def testComputeRank():
    avl, root = createTree()
    printAVLTree(avl, True)
    for key in range(19):
        print("Rank of element with the key {} is:".format(key), end=' ')
        print(AVL.computeRank(avl.getRoot(), avl, key))
        print()


#testComputeRank()
