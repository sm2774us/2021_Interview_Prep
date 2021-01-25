"""
Iterative version
This version assumes that keys of all nodes in a tree are different, that they don't repeat.
Uncomment desired test calls.
"""

import BST_Iter as BST


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


def createTree():
    """We can do it like this..."""
    n1 = BST.Node(1)
    n4 = BST.Node(4)
    n6 = BST.Node(6)
    n7 = BST.Node(7)    # root
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
    bst.insert(4)
    bst.insert(1)
    bst.insert(6)
    bst.insert(13)
    bst.insert(15)
    bst.insert(10)

    return bst, root


def createTree():
    """...And probably the best this way!"""

    # We must create the root node first!
    # Then we create the BST tree with that root node.
    bst = BST.BinarySearchTree(BST.Node(7))

    # Only now can we add other nodes; we couldn't before creating the BST tree! We must use insert() method!
    bst.insert(4)
    bst.insert(1)
    bst.insert(6)
    bst.insert(13)
    bst.insert(15)
    bst.insert(10)

    return bst, bst.getRoot()


def testTree():
    bst, root = createTree()

    print("\nPrint:")
    print("In order:  ", bst.inOrder())
    print("Pre order: ", bst.preOrder())
    print("Post order:", bst.postOrder())
    print("BFS:       ", bst.BFS())
    print("Root:", end=' ')
    root.printNode()

    print("\nFind:")
    print(0, bst.find(0))
    print(1, bst.find(1))
    print(2, bst.find(2))
    print(5, bst.find(5))
    print(6, bst.find(6))
    print(7, bst.find(7))
    print(8, bst.find(8))
    print(12, bst.find(12))
    print(13, bst.find(13))
    print(14, bst.find(14))
    print(15, bst.find(15))
    print(20, bst.find(20))

    print("\nNext:")
    print(0, bst.next(bst.find(0)))
    print(1, bst.next(bst.find(1)))
    print(2, bst.next(bst.find(2)))
    print(4, bst.next(bst.find(4)))
    print(5, bst.next(bst.find(5)))
    print(6, bst.next(bst.find(6)))
    print(7, bst.next(bst.find(7)))
    print(8, bst.next(bst.find(8)))
    print(10, bst.next(bst.find(10)))
    print(12, bst.next(bst.find(12)))
    print(14, bst.next(bst.find(14)))
    print(15, bst.next(bst.find(15)))
    print(16, bst.next(bst.find(16)))

    print("\nPrevious:")
    print(0, bst.previous(bst.find(0)))
    print(1, bst.previous(bst.find(1)))
    print(2, bst.previous(bst.find(2)))
    print(4, bst.previous(bst.find(4)))
    print(5, bst.previous(bst.find(5)))
    print(6, bst.previous(bst.find(6)))
    print(7, bst.previous(bst.find(7)))
    print(8, bst.previous(bst.find(8)))
    print(10, bst.previous(bst.find(10)))
    print(12, bst.previous(bst.find(12)))
    print(14, bst.previous(bst.find(14)))
    print(15, bst.previous(bst.find(15)))
    print(16, bst.previous(bst.find(16)))

    print("\nRange search:")
    print(5, 12)
    for node in bst.rangeSearch(5, 12):
        print(node, end=' ')
    print()

    if 0:                                   # put 1 to execute this
        print("\nInsert:")
        print("In order:  ", bst.inOrder())
        print("Pre order: ", bst.preOrder())
        print("BFS:       ", bst.BFS())
        n = 3                               # key of the node to insert
        bst.insert(n)
        node = bst.find(n)
        node.printNode()
        node.getParent().printNode()
        print("Inserting", n)
        print("In order:  ", bst.inOrder())
        print("Pre order: ", bst.preOrder())
        print("BFS:       ", bst.BFS())

        print()
        print("In order:  ", bst.inOrder())
        print("Pre order: ", bst.preOrder())
        print("Post order:", bst.postOrder())
        print("BFS:       ", bst.BFS())
        n = 5                               # key of the node to insert
        bst.insert(n)
        node = bst.find(n)
        node.printNode()
        node.getParent().printNode()
        print("Inserting", n)
        print("In order:  ", bst.inOrder())
        print("Pre order: ", bst.preOrder())
        print("Post order:", bst.postOrder())
        print("BFS:       ", bst.BFS())

    if 0:                                   # put 1 to execute this
        print("\nDelete:")
        print("In order:  ", bst.inOrder())
        print("Pre order: ", bst.preOrder())
        print("BFS:       ", bst.BFS())
        n = 7                                   # key of the node to delete (make sure to try with the root node!)
        bst.delete(bst.find(n))                 # We don't need to reassign the root, even in the case when we're deleting the root node!
        print("Deleting", n)
        print("In order:  ", bst.inOrder())
        print("Pre order: ", bst.preOrder())
        print("BFS:       ", bst.BFS())
        print("This is the node under which the deleted node, {}, would come: {}.".format(n, bst.find(n)))
        bst.find(n).printNode()
        try:
            bst.find(n).getParent().printNode()
        except:
            print("New root:", end=' ')
            bst.find(root.getKey()).printNode()
        print("Root is:", end=' ')
        bst.getRoot().printNode()

    print("\nRotate right:")
    printTree(bst, True)
    n = 7                                       # key of the node to rotate (make sure to try with the root node!)
    bst.rotateRight(bst.find(n))                # We don't need to reassign the root, even in the case when we're deleting the root node!
    print("Rotating right", n)
    printTree(bst, True)
    bst.find(n).printNode()

    print("\nRotate left:")
    printTree(bst, True)
    n = 1                                       # key of the node to rotate (make sure to try with the root node!)
    bst.rotateLeft(bst.find(n))                 # We don't need to reassign the root, even in the case when we're deleting the root node!
    print("Rotating left", n)
    printTree(bst, True)
    bst.find(n).printNode()



def test1():
    bst = BST.BinarySearchTree(BST.Node(3))     # root
    bst.insert(1)
    bst.insert(4)
    bst.insert(5)
    printTree(bst, True)
    bst.delete(bst.find(3))
    printTree(bst, True)


def test2():
    bst, root = createTree()
    printTree(bst, True)
    bst.delete(bst.find(7))
    printTree(bst, True)



testTree()
#test1()
#test2()