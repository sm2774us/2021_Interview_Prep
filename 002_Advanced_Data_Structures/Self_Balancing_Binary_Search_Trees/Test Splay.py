import Splay

printTree = Splay.printTree


def test0():
    """Empty tree"""
    print("Empty tree\n")
    tree = Splay.SplayTree()
    print(tree)
    print(tree.getRoot())
    print(tree.find(4))
    printTree(tree, True)

def test1():
    """Adding one element, then deleting it."""
    print("Adding one element, then deleting it\n")
    tree = Splay.SplayTree()
    tree.insert(7)
    print(tree)
    print(tree.getRoot())
    print(4, tree.find(4))
    print(7, tree.find(7))
    print(9, tree.find(9))
    printTree(tree, True)
    print("Deleting the only element.\n")
    tree.delete(7)
    print(tree)
    print(tree.getRoot())
    print(7, tree.find(7))
    printTree(tree, True)

def test2():
    tree = Splay.SplayTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    printTree(tree, True)
    print(tree)
    n = 2
    print("\n\nFinding {}, which should splay it up to the top.".format(n))
    tree.find(n)
    printTree(tree, True)
    print(tree)
    return tree

def test3():
    tree = test2()
    print("\n\nFinding 777, which is not there.")
    tree.find(777)
    printTree(tree, True)
    print(tree)

    print("\n\nFinding 0, which is not there.")
    tree.find(0)
    printTree(tree, True)
    print(tree)

    n = 777
    print("\n\nDeleting 777, which is not there.")
    tree.delete(777)
    printTree(tree, True)
    print(tree)

    n = 3
    print("\n\nDeleting {}, which is there.".format(n))
    tree.delete(n)
    printTree(tree, True)
    print(tree)

def test4():
    tree = Splay.SplayTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(6)
    tree.insert(5)
    printTree(tree, True)
    print(tree)

    n = 2
    print("\n\nDeleting {}, which is there.".format(n))
    tree.delete(n)
    printTree(tree, True)
    print(tree)

def createTree1():
    """Nodes from Berkeley CS 61B - Tree 1, but the tree doesn't look the same. Use the visualization site."""
    tree = Splay.SplayTree()
    tree.insert(7)
    tree.insert(1)
    tree.insert(11)
    tree.insert(0)
    tree.insert(5)
    tree.insert(9)
    tree.insert(12)
    tree.insert(3)
    tree.insert(6)
    tree.insert(8)
    tree.insert(10)
    tree.insert(2)
    tree.insert(4)
    return tree

def createTree2():
    """Berkeley CS 61B - Tree 2"""
    tree = Splay.SplayTree()
    tree.insert(0)
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(10)
    tree.insert(9)
    return tree

def test5():
    tree = createTree1()
    #tree = createTree2()

    printTree(tree, True)
    print(tree)

    if 0:                                               # put 1 to execute this
        print("\nPrint:")
        print("In order:  ", tree.inOrder())
        print("Pre order: ", tree.preOrder())
        print("Post order:", tree.postOrder())
        print("Level order:       ", tree.levelOrder())

    if 0:                                               # put 1 to execute this
        n = 1
        print("\n\nFinding {}, which should splay it up to the top.".format(n))
        tree.find(n)
        printTree(tree, True)
        print(tree)

    if 0:                                               # put 1 to execute this
        print("\nNext:")
        print(0, tree.next(0))
        print(1, tree.next(1))
        print(2, tree.next(2))
        print(3, tree.next(3))
        print(4, tree.next(4))
        print(5, tree.next(5))
        print(6, tree.next(6))
        print(7, tree.next(7))
        print(8, tree.next(8))
        print(9, tree.next(9))
        print(10, tree.next(10))
        print(11, tree.next(11))
        print(12, tree.next(12))
        print(15, tree.next(15))

    if 0:                                               # put 1 to execute this
        print("\nRange search:")
        m, n = -1, 20
        print(m, n)
        for node in tree.rangeSearch(m, n):
            print(node, end=' ')
        print()
        printTree(tree, True)
        print(tree)

    if 0:                                               # put 1 to execute this
        n = 9
        print("\n\nDeleting {}, which is there.".format(n))
        tree.delete(n)
        printTree(tree, True)
        print(tree)


#test0()
#test1()
#test2()
#test3()
#test4()
#test5()


def testMerge1():
    tree1 = Splay.SplayTree()
    tree1.insert(7)
    tree1.insert(3)
    tree1.insert(13)
    tree1.insert(1)
    tree1.insert(5)
    tree1.insert(10)
    tree1.insert(15)
    tree1.insert(17)
    tree1.insert(4)
    tree1.insert(6)
    tree1.insert(11)
    printTree(tree1, True)

    tree2 = Splay.SplayTree()
    tree2.insert(18)
    tree2.insert(20)
    tree2.insert(22)
    printTree(tree2, True)

    tree1 = Splay.merge(tree1, tree2)
    del tree2
    printTree(tree1, True)
    return tree1

def testMerge2():
    tree1 = Splay.SplayTree()
    tree1.insert(5)
    tree1.insert(3)
    tree1.insert(1)
    tree1.insert(2)
    printTree(tree1, True)

    tree2 = Splay.SplayTree()
    tree2.insert(12)
    tree2.insert(8)
    tree2.insert(14)
    tree2.insert(7)
    tree2.insert(10)
    tree2.insert(13)
    tree2.insert(15)
    tree2.insert(9)
    tree2.insert(11)
    printTree(tree2, True)

    tree1 = Splay.merge(tree1, tree2)
    del tree2
    printTree(tree1, True)
    return tree1


#testMerge1()
#testMerge2()


def testSplit1():
    tree = testMerge1()
    x = 15
    print("\nSplitting the tree at {}.\n".format(x))
    tree1, tree2 = Splay.split(tree, x)
    del tree
    printTree(tree1, True)
    print(tree1)
    printTree(tree2, True)
    print(tree2)

def testSplit2():
    tree = testMerge2()
    x = 6
    print("\nSplitting the tree at {}.\n".format(x))
    tree1, tree2 = Splay.split(tree, x)
    del tree
    printTree(tree1, True)
    print(tree1)
    printTree(tree2, True)
    print(tree2)



#testSplit1()
#testSplit2()



def testOrderStatistic1():
    tree = createTree1()
    printTree(tree, True)
    print(tree)
    k = 13
    print("\n{}. element is:".format(k), end=' ')
    print(tree._orderStatisticRecursive(tree.getRoot(), k))

def testOrderStatistic2():
    tree = createTree2()
    printTree(tree, True)
    print(tree)
    k = 6
    print("\n{}. element is:".format(k), end=' ')
    node = tree._orderStatisticRecursive(tree.getRoot(), k)
    print(node)
    tree._splay(node)
    printTree(tree, True)
    print(tree)
    print("\n{}. element is:".format(k), end=' ')
    node = tree._orderStatisticRecursive(tree.getRoot(), k)
    print(node)

def testOrderStatistic3():
    tree = Splay.SplayTree()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(6)
    tree.insert(5)
    tree.insert(4)
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    printTree(tree, True)
    print(tree)
    k = 6
    print("\n{}. element is: {}.".format(k, tree._orderStatisticRecursive(tree.getRoot(), k)))
    print("{}. element is: {}.".format(k, tree._orderStatistic(k)))
    print("{}. element is: {}.".format(k, tree.orderStatistic(k)))


#testOrderStatistic1()
#testOrderStatistic2()
#testOrderStatistic3()


def testOrderStatisticZero():
    """Run it in pair with testOrderStatistic3()."""
    tree = Splay.SplayTree()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(6)
    tree.insert(5)
    tree.insert(4)
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    printTree(tree, True)
    print(tree)
    k = 5
    print("\n{}. element, if we count from 1, is: {}.".format(k+1, tree._orderStatisticZeroBasedRankingRecursive(tree.getRoot(), k)))
    print("{}. element, if we count from 1, is: {}.".format(k+1, tree._orderStatisticZeroBasedRanking(k)))
    print("{}. element, if we count from 1, is: {}.".format(k+1, tree.orderStatisticZeroBasedRanking(k)))
    print("But that element has index {} if we count from 0.".format(k))


#testOrderStatisticZero()


def testComputeRank1():
    tree = createTree1()
    printTree(tree, True)
    print(tree)
    print()
    for key in range(15):
        print("Rank of element with the key {} is:".format(key), end=' ')
        print(tree.computeRank(tree.getRoot(), key))
        print()

def testComputeRank2():
    tree = createTree2()
    printTree(tree, True)
    print(tree)
    print()
    for key in range(15):
        print("Rank of element with the key {} is:".format(key), end=' ')
        print(tree.computeRank(tree.getRoot(), key))
        print()


#testComputeRank1()
#testComputeRank2()
