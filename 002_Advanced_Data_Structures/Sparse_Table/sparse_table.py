import math


class SparseTable(object):
    """
        TODO: add a flag to switch min/max
    """
    LOG_TWO_N = 20  # 2 ^ 20 > 1000000

    def __init__(self, A):
        self.n = len(A)
        self.SpT = [[-1] * SparseTable.LOG_TWO_N for i in range(len(A))]
        self.A = list(A)
        for i in range(len(A)):
            self.SpT[i][0] = i
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1 < self.n):
                if self.A[self.SpT[i][j - 1]] > self.A[self.SpT[i + (1 << (j - 1))][j - 1]]:
                    self.SpT[i][j] = self.SpT[i][j - 1]
                else:
                    self.SpT[i][j] = self.SpT[i + (1 << (j - 1))][j - 1]
                i += 1
            j += 1

    def query(self, i, j):
        k = int(math.floor(math.log(float(j - i + 1)) * 1.0 / math.log(2.0)))
        if self.A[self.SpT[i][k]] >= self.A[self.SpT[j - (1 << k) + 1][k]]:
            return self.SpT[i][k]
        else:
            return self.SpT[j - (1 << k) + 1][k]


A = [18, 17, 13, 19, 15, 11, 20]
st = SparseTable(A)
import pprint

pprint.pprint(st.SpT)