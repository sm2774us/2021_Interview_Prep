"""
When both union by rank heuristic and path compression heuristic are used, the average running time of each operation is nearly constant.
"""

class DisjointSet(object):
    
    def __init__(self, n):
        """
        n is the number of elements.
        Efficient implementation
        Uses Trees, Union by Rank Heuristic, and Path Compression Heuristic.
        Uses 1-based indexing of arrays.
        """
        self.n = n
        self.parent = [None] * (n + 1)
        self.rank = [None] * (n + 1)

    def makeSet(self, i):
        """Makes a set of element i."""
        self.parent[i] = i
        self.rank[i] = 0

    #def find(self, i):
    #    """Union by Rank Heuristic
    #    O(log n)
    #    """
    #    while i != self.parent[i]:
    #        i = self.parent[i]
    #    return i

    def find(self, i):
        """Path Compression Heuristic
        O(log* n) = O(1)
        """
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """Union by Rank Heuristic
        Merges sets with i and j."""
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

    def __str__(self):
        print("i:        ", end=' ')
        for i in range(1, self.n + 1):
            print('{:2d}'.format(i), end=' ')
        print()
        print("parent[i]:", end=' ')
        for p in self.parent[1:]:
            print('{:2d}'.format(p), end=' ')
        print()
        print("rank[i]:  ", end=' ')
        for r in self.rank[1:]:
            print('{:2d}'.format(r), end=' ')
        print()
        return ""



def example1():
    dj = DisjointSet(6)
    for i in range(1, 7):
        dj.makeSet(i)
    print(dj)
    dj.union(2, 4)
    print(dj)
    dj.union(5, 2)
    print(dj)
    dj.union(3, 1)
    print(dj)
    dj.union(2, 3)
    print(dj)
    dj.union(2, 6)
    print(dj)

def example2():
    dj = DisjointSet(12)
    for i in range(1, 13):
        dj.makeSet(i)
    dj.union(10, 5)
    print(dj)
    dj.union(7, 10)
    print(dj)
    dj.union(3, 5)
    print(dj)
    dj.union(12, 3)
    print(dj)
    dj.union(12, 6)
    print(dj)
    dj.union(1, 6)
    print(dj)
    dj.union(11, 6)
    print(dj)
    dj.union(8, 12)
    print(dj)
    dj.union(3, 2)
    print(dj)
    dj.union(9, 5)
    print(dj)
    dj.union(4, 9)
    print(dj)
    print(dj).find(6)
    print(dj)

def ex1():
    dj = DisjointSet(12)
    for i in range(1, 13):
        dj.makeSet(i)
    dj.union(2, 10)
    print(dj)
    dj.union(7, 5)
    print(dj)
    dj.union(6, 1)
    print(dj)
    dj.union(3, 4)
    print(dj)
    dj.union(5, 11)
    print(dj)
    dj.union(7, 8)
    print(dj)
    dj.union(7, 3)
    print(dj)
    dj.union(12, 2)
    print(dj)
    dj.union(9, 6)
    print(dj)
    print(dj).find(6)
    print(dj)
    print(dj).find(3)
    print(dj)
    print(dj).find(11)
    print(dj)
    print(dj).find(9)
    print(dj)

def ex2():
    ex1()

def ex3():
    dj = DisjointSet(10)
    for i in range(1, 11):
        dj.makeSet(i)
    for i in range(1, 10):
        dj.union(i, i+1)
        print(dj)

def ex4():
    dj = DisjointSet(60)
    for i in range(1, 61):
        dj.makeSet(i)
    for i in range(1, 31):
        dj.union(i, 2*i)
    for i in range(1, 21):
        dj.union(i, 3*i)
    for i in range(1, 13):
        dj.union(i, 5*i)
    for i in range(1, 61):
        dj.find(i)
    print(dj)


if __name__ == "__main__":
    example1()
    #example2()
    #ex1()
    #ex2()
    #ex3()
    #ex4()

