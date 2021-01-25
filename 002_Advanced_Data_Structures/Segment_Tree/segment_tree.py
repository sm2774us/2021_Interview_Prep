class SegmentTree(object):
    """ Min/Max segment tree"""

    def __init__(self, A, isMin=True):
        self.st = [0] * (4 * len(A))
        self.A = list(A)
        self.n = len(A)
        self.isMin = isMin
        self.build(1, 0, self.n - 1)

    def left(self, p):
        return p << 1

    def right(self, p):
        return (p << 1) + 1

    def build(self, p, left, right):
        if left == right:
            self.st[p] = left
        else:
            self.build(self.left(p), left, (left + right) // 2)
            self.build(self.right(p), (left + right) // 2 + 1, right)
            p1, p2 = self.st[self.left(p)], self.st[self.right(p)]
            if self.isMin:
                self.st[p] = p1 if self.A[p1] <= self.A[p2] else p2
            else:
                self.st[p] = p1 if self.A[p1] >= self.A[p2] else p2

    def rmq(self, i, j):
        return self._rmq(1, 0, self.n - 1, i, j)

    def _rmq(self, p, L, R, i, j):
        if i > R or j < L: return -1
        if L >= i and R <= j: return self.st[p]
        p1 = self._rmq(self.left(p), L, (L + R) // 2, i, j)
        p2 = self._rmq(self.right(p), (L + R) // 2 + 1, R, i, j)
        if p1 == -1: return p2
        if p2 == -1: return p1
        if self.isMin:
            if self.A[p1] <= self.A[p2]:
                return p1
            else:
                return p2
        else:
            if self.A[p1] >= self.A[p2]:
                return p1
            else:
                return p2

    def update(self, idx, new_value):
        return self._update(1, 0, self.n - 1, idx, new_value)

    def _update(self, p, L, R, idx, new_value):
        i = idx
        j = idx
        if i > R or j < L: return self.st[p]
        if L == i and R == j:
            self.A[i] = new_value
            self.st[p] = L
            return L

        p1 = self._update(self.left(p), L, (L + R) // 2, idx, new_value)
        p2 = self._update(self.right(p), (L + R) // 2 + 1, R, idx, new_value)
        if self.isMin:
            self.st[p] = p1 if self.A[p1] <= self.A[p2] else p2
        else:
            self.st[p] = p1 if self.A[p1] >= self.A[p2] else p2
        return self.st[p]


if __name__ == "__main__":
    A = [18, 17, 13, 19, 15, 11, 20]
    st = SegmentTree(A)
    assert (st.rmq(1, 3) == 2)
    assert (st.rmq(0, 6) == 5)
    assert (st.rmq(4, 6) == 5)
    assert (st.rmq(0, 0) == 0)
    assert (st.rmq(6, 6) == 6)
    assert (st.update(0, -1) == 0)
    assert (st.update(0, 18) == 5)
    assert (st.update(5, 30) == 2)

    st2 = SegmentTree(A, False)
    assert (st2.rmq(1, 3) == 3)
    assert (st2.rmq(0, 6) == 6)
    assert (st2.update(2, 30) == 2)
    print("Passed all tests!")