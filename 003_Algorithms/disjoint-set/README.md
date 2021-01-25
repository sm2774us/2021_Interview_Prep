

A [disjoint-set](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) data structure, also called a **union–find** data structure or **merge–find set**, is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. It provides near-constant-time operations to add new sets, to merge existing sets, and to determine whether elements are in the same set. It plays a key role in Kruskal's algorithm for finding the minimum spanning tree of a graph.

Implementation
---------------

1. **Quick-Find**: In this implementation of the disjoint-set data structure the `find()` operation is quick because it only needs to access the elements of a list. The problem with this implementation is that `union()` needs to scan through the whole `id[]` array for each input pair in order to apply the union operator when needed. This operation must be done in all the cases.

2. **Quick-Union**: In this implementation of the disjoint-set data structure we focus on speeding up the `union()` operation.  To implement `find()`, we start at the given site, follow its link to another site, follow that site’s link to yet another site, and so forth, following links until reaching a root, a site that has a link to itself (which is guaranteed to happen). Two sites are in the same component if and only if this process leads them to the same root. The quick-union algorithm would seem to be faster than the quick-find algorithm, because it does not have to go through the entire array for each input pair; However in the worst case scenario it will have to iterate through the entire array before finding a root node, for instance in a structure like: `1>2>3>4>5>6>7>8` when the function `union(7,8)` is called it has to iterate back to the root 1 and scan the entire array leading to complexity O(N^2). You can regard quick-union as an improvement over quick-find because it removes quick-find main liability (that `union()` always takes linear time). This difference certainly represents an improvement for typical data, but quick-union still has the liability that we cannot guarantee it to be  substantially faster than quick-find in every case

3. **Weighted-Union**: In this implementation of the disjoint-set data structure we focus on optimizing the union operation when two trees are joined in a common set. Merging a short tree with the large one, it is possible to keep contained the depth of the resulting tree. This simple trick allows reducing the complexity to O(log N). This improvement requires a new array in order to store the size of the set.


Methods
--------

- `find()`: it returns the identifier of a given set.
- `union()`: it merges two components and decrement the set counter.
- `connected()`: it determines if two elements are in the same set.
- `count()`: it retunrs the number of current sets.

Material
--------
- **Coursera Algorithms Part 1**: week 1
- **Algorithms**, Sedgewick and Wayne (2014): Chapter 1.5

