# A 1-indexed Bit Indexed Tree or Fenwick Tree
class FenwickTree:
	# Modifies list a in place, builds Fenwick tree out of frequency table in O(n) time, n = len(a)
	# Why not O(n log n)? Because we are going from left to right in the array,
	# from leave to root in the tree, we can propagate the values up the tree 1 parent node at a time
	def __init__(self, a):
		# Shifts index 0 to index 1 to avoid infinite recursion -> index 0 + LSOne(0) is still 0
		for (idx,v) in enumerate(a):
			nextIdx = (idx+1) + lowestSetBit(idx+1) - 1
			if nextIdx < len(a):
				a[nextIdx] += v
		self.tree = a

	def __str__(self):
		return str(self.tree)

	# Find the sum of elements from start of array to idx, inclusive
	def prefixSum(self, idx):
		if idx < 1: raise Exception("Invalid index, must be at least 1")
		if idx > len(self.tree): raise Exception("Index out of bounds exception")
		ans = 0
		while idx > 0:
			ans += self.tree[idx-1]
			idx -= lowestSetBit(idx)
		return ans

	# Find the sum of elements from start to end inclusive
	def range(self, start, end):
		if start < 1:
			raise Exception("Starting index must be at least 1.")
		if end < start:
			raise Exception("End index must be greater than or equal to start")
		if start == 1:
			return self.prefixSum(end)
		else:
			return self.prefixSum(end) - self.prefixSum(start-1)

	# idx of a 1-based array, delta is amount to increment or decrement
	def update(self, idx, delta):
		if idx < 1: raise Exception("Invalid index, must be at least 1")
		if idx > len(self.tree): raise Exception("Index out of bounds exception")
		while idx <= len(self.tree):
			self.tree[idx-1] += delta
			idx += lowestSetBit(idx)

	# idx of a 1-based array, value is new value to update to
	def updateToValue(self, idx, value):
		if idx < 1: raise Exception("Invalid index, must be at least 1")
		if idx > len(self.tree): raise Exception("Index out of bounds exception")
		delta = value - self.tree[idx-1]
		while idx <= len(self.tree):
			self.tree[idx-1] += delta
			idx += lowestSetBit(idx)

	# Support for Range Update, Point Query and Range Update, Range Query
	# Useful for tracking intervals and querying how many intersections within the interval
	# a, b is interval, inclusive, delta is amount to increment or decrement
	def rangeUpdate(self, a, b, delta):
		if a < 1: raise Exception("Invalid index, must be at least 1")
		if b > len(self.tree): raise Exception("Index out of bounds exception")
		if a > b: raise Exception("Invalid index, lower bound index is greater than upper bound index")
		self.update(a, delta)
		if b+1 <= len(self.tree): self.update(b+1, -delta)

	def pointQuery(self, idx):
		if idx < 1: raise Exception("Invalid index, must be at least 1")
		if idx > len(self.tree): raise Exception("Index out of bounds exception")
		return self.prefixSum(idx)

	# Given the element (index / score), return the cumulative frequency, i.e. how many people scored less than or equal to this score
	def rank(self, x):
		return self.prefixSum(x)

	# Given the rank k (frequency), returns the kth smallest element (index) in the tree
	def select(self, k):
		l = 0
		r = len(self.tree) - 1
		while l < r:
			mid = (l + r) / 2
			if k <= self.prefixSum(mid+1):
				r = mid
			else:
				l = mid + 1
		return l + 1 # convert to 1-based index

def lowestSetBit(intType):
	return (intType & -intType)

# Updates 2 Fenwick Trees for RURQ
def update(t1, t2, a, b, delta):
	t1.rangeUpdate(a, b, delta)
	if a > 0: t2.update(a, (a-1)*delta)
	if b+1 <= len(t2.tree): t2.update(b+1, -b*delta)

def rangeSum(t1, t2, a, b):
	if a <= 1:
		return (t1.pointQuery(b) * b - t2.pointQuery(b))
	else:
		return (t1.pointQuery(b) * b - t2.pointQuery(b)) - (t1.pointQuery(a-1) * (a-1) - t2.pointQuery(a-1))

def test():
	import copy
	a = [1,2,3,4,5,6,7,8,9,10]
	tree = FenwickTree(copy.deepcopy(a))
	assert(tree.tree == [1,3,3,10,5,11,7,36,9,19])
	# print(tree)

	assert(tree.prefixSum(1) == 1)
	assert(tree.prefixSum(10) == 55)
	try:
		tree.prefixSum(0)
	except Exception as e:
		assert(e.message == "Invalid index, must be at least 1")
	try:
		assert(tree.prefixSum(-1) == 0)
	except Exception as e:
		assert(e.message == "Invalid index, must be at least 1")

	assert(tree.range(1,4) == 10)
	assert(tree.range(2,5) == 14)
	assert(tree.range(5, 10) == 45)

	tree.update(1, 9)
	assert(tree.tree == [10,12,3,19,5,11,7,45,9,19])
	assert(tree.range(1,4) == 19)
	assert(tree.range(2,5) == 14)
	assert(tree.range(5, 10) == 45)

	# Test rank, select
	# Imagine this is a frequency table of test scores -> num of students. index of array corresponds to test score
	a = [0,0,1,0,1,2,3,2,1,1,0]
	# Cumulative frequency table = [0,0,1,1,2,4,7,9,10,11,11]
	tree = FenwickTree(copy.deepcopy(a))
	assert(tree.rank(1) == 0)
	assert(tree.rank(5) == 2) # Actually it means score of 4 in our 1-indexed array
	assert(tree.rank(10) == 11)
	assert(tree.rank(11) == 11)
	tree.update(1,1)
	assert(tree.rank(1) == 1)
	assert(tree.rank(5) == 3) # Actually it means score of 4 in our 1-indexed array
	assert(tree.rank(10) == 12)
	assert(tree.rank(11) == 12)

	tree = FenwickTree(copy.deepcopy(a))
	assert(tree.select(0) == 1)
	assert(tree.select(1) == 3)
	assert(tree.select(2) == 5)
	assert(tree.select(11) == 10)
	assert(tree.select(6) == 7)
	assert(tree.select(3) == 6)
	assert(tree.select(15) == 11)

	# Test RU,PQ (range update, point query)
	a = [0,0,0,0,0,0,0,0,0,0]
	tree = FenwickTree(copy.deepcopy(a))
	assert(tree.tree == a)
	tree.rangeUpdate(1,2,1)
	assert(tree.pointQuery(3) == 0)
	assert(tree.pointQuery(1) == 1)
	tree.rangeUpdate(1,3,1)
	assert(tree.pointQuery(1) == 2)
	assert(tree.pointQuery(3) == 1)
	tree.rangeUpdate(5,10, 1)
	assert(tree.pointQuery(4) == 0)
	assert(tree.pointQuery(5) == 1)
	assert(tree.pointQuery(10) == 1)
	tree.rangeUpdate(9,9,1)
	assert(tree.pointQuery(10) == 1)
	assert(tree.pointQuery(9) == 2)

	# Test RU, RQ (range update, range query) We need to maintain 2 Fenwick trees
	a = [0,0,0,0,0,0,0,0,0,0]
	t1 = FenwickTree(copy.deepcopy(a))
	t2 = FenwickTree(copy.deepcopy(a))
	update(t1,t2,1,2,1)
	assert(rangeSum(t1,t2,1,2) == 2)
	update(t1,t2,1,3,1)
	assert(rangeSum(t1,t2,1,3) == 5)
	update(t1,t2,5,10,1)
	assert(rangeSum(t1,t2,4,10) == 6)
	assert(rangeSum(t1,t2,7,10) == 4)
	assert(rangeSum(t1,t2,3,6) == 3)
	update(t1,t2,9,9,1)
	assert(rangeSum(t1,t2,10,10) == 1)
	assert(rangeSum(t1,t2,9,9) == 2)
	assert(rangeSum(t1,t2,0,1) == 2)

	print("All tests passed!")

if __name__ == "__main__":
	test()