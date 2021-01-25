# Sorting

## Bubblesorts
**Definition:** Simple comparison based algorithms. Each pair of adjacent elements are compared and swapped, if need be.

**When to Use:**
* Need a simple sorting method
* Time complexity is not a concern

**Complexity:**

| |Time|Space|
|:---|:---|:---|
|**Best**|Ω(n)||
|**Average**|θ(n<sup>2</sup>)||
|**Worst**|O(n<sup>2</sup>)|O(1)|

<br/>

## Simple Sorts
**Definition:** Efficient sort when there is a small number of elements, but inefficient on larger sets.

### Insertion Sort
Each element of an unsorted array is placed in sorted order, one by one, until all elements are sorted. Can be done in-place, but requires shifting.

**When to Use:**
* Small number of elements to sort
* Elements are nearly in sorted order
* Number of writes is not restricted (outperforms selection sort)

**Complexity:**

| |Time|Space|
|:---|:---|:---|
|**Best**|Ω(n)||
|**Average**|θ(n<sup>2</sup>)||
|**Worst**|O(n<sup>2</sup>)|O(1)|

<br/>

### Selection Sort
Finds the minimum element in the array and swaps it with the current position, which starts out at the beginning of the array and is incremented after each minimum element is found until the end of the array is reached.

**When to Use:**
* Small number of elements to sort
* Performance is important
  * Smaller number of writes 

**Complexity:**

| |Time|Space|
|:---|:---|:---|
|**Best**|Ω(n<sup>2</sup>)||
|**Average**|θ(n<sup>2</sup>)||
|**Worst**|O(n<sup>2</sup>)|O(1)|

<br/>

## Efficient Sorts
**Definition:** On average these algorithms perform in θ(nlog(n)), making them practical for most cases.

### Merge Sort
A stable, divide and conquer sorting algorithm. An array of size n is divided into n sublists, each containing 1 element. The sublists are paired and merged into new sorted sublists, effectively halving the number of sublists and doubling each sublists' size. The sublists continue to pair and merge until only one sorted list is left. 

**When to Use:**
* Require a stable sort
  * [\[5, 2], [5, 1], [3, 0], [10, 11]] => [[3, 0], [5, 2], [5, 1], [10, 11]\]
    * Stability means that the order among elements of the same comparison value is maintained
    * Notice that [5, 1] comes after [5, 2] \([5, 2], [5, 1] instead of [5, 1], [5, 2]) in the resulting array
* Need guaranteed O(nlog(n)) 

**Complexity:**

| |Time|Space|
|:---|:---|:---|
|**Best**|Ω(nlog(n))||
|**Average**|θ(nlog(n))||
|**Worst**|O(nlog(n))|O(n)|

<br/>

### Quicksort
The most popular efficient sorting algorithm, which applies a divide and conquer methodology. A pivot position is selected in an array, and elements less than the value at the pivot are ordered before the pivot, while elements greater than the value at the pivot are ordered after the pivot. That pivot is now in its final position. This is done recursively for each subarray that is created to the left and right of the previous pivots until every pivot is in its final position. 

**When to Use:**
* Do not require stable sort
* Average case is priority (average case will beat both merge sort and heapsort)
* Require in-place sorting

**Complexity:**

| |Time|Space|
|:---|:---|:---|
|**Best**|Ω(nlog(n))||
|**Average**|θ(nlog(n))||
|**Worst**|O(n<sup>2</sup>)|O(1)|

<br/>

### Heapsort
Same as an insertion sort, except the maximum value is found using a heap instead of an linear search. An array is splity into an unsorted region and a sorted region, and a heap is constructed from the elements of the unsorted region. The maximum value of the unsorted region is found and placed into the sorted region, and this is done until every element is in the sorted region (O(n)). The heap improves on the search time for finding the maximum value in the unsorted data to O(log(n)).  

**When to Use:**
* Do not require stable sort
* Worst case is priority
* Require in-place sorting

**Complexity:**

| |Time|Space|
|:---|:---|:---|
|**Best**|Ω(nlog(n))||
|**Average**|θ(nlog(n))||
|**Worst**|O(nlog(n))|O(1)|

<br/>

## Distribution Sorts
**Definition:** Relies on the properties of the data structures' used to contain the elements. Elements are not compared amongst each other, rather their data structures are compiled into the output.

### Bucket Sort
Elements are distributed among an array of buckets, and each filled bucket is then sorted. In sequential order, each filled bucket's contents are output to the original array.  

**When to Use:**
* Data is uniformly distributed

**Complexity:**

| |Time|Space|
|:---|:---|:---|
|**Best**|Ω(n+k)||
|**Average**|θ(n+k)||
|**Worst**|O(n<sup>2</sup>)|O(1)|

<br/>

### Counting Sort
Each element being sorted has an associated key, and each distinct key is counted. Each count of the distinct keys is run through a hash to determine their final sorted position. 

**When to Use:**
* Range of data is not significantly greater than the number of elements in data 


**Complexity:**

| |Time|Space|
|:---|:---|:---|
|**Best**|Ω(n+k)||
|**Average**|θ(n+k)||
|**Worst**|O(n+k)|O(k)|

<br/>

### Radix Sort
Each significant position of an element is assigned an integer key. Starting with the least significant digit, the values are individually placed into buckets based on their integer key, and values placed in the same bucket maintain their original ordering (stable sort). This process is repeated until the last significant position is grouped into a bucket. 

**When to Use:**
* Number of significant digits in the greatest number, k, is less than the number of keys, n. 

**Complexity:**

| |Time|Space|
|:---|:---|:---|
|**Best**|Ω(nk)||
|**Average**|θ(nk)||
|**Worst**|O(nk)|O(k)|

***

<br/>

# Algorithms Part I
-----------------

Collection of algorithms and data structures implemented in Python and C++. For an optimal learning experience it is recommended to study the material in the following order:

1. **Disjoint-set**: (data structure) [[link]](./disjoint-set)

2. **Stack**: (abstract data structure) [[link]](./stack)

3. **Queue**: (abstract data structure) [[link]](./queue)

4. **Elementary sort**: (sorting algorithm) TBD [selection sort, insertion sort, shellsort]

5. **Mergesort**: (sorting algorithm) [[link]](./mergesort)

6. **Quicksort**: (sorting algorithm) [[link]](./quicksort)

7. **Priority-Queue**: (data structure) similarly to a Queue it stores an array of values, but when `pop()` is called the largest value (higher priority) is returned [[link]](./priority-queue)

8. **Symbol Tables**: (data structure) the primary purpose is to associate a key to a value. The best standard implementation is based on ordered arrays and has O(log N) time complexity for `get()` and O(N) time complexity for `put()` [[link]](./symbol-tables)

9. **Binary Search Trees (BSTs)**: (data structure) it is a smart implementation of symbol tables. It solves the problem given by the standard symbol table implementations, giving O(log N) time complexity for both `get()` and `put()`. [[link]](./binary-search-trees)

10. **Balanced Search Trees**: (data structure) it solves the problem of unbalanced trees, given by standard BSTs. It is also known as [self-balancing](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree) binary search tree. The problem with this data structure is the overhead in keeping track of different types of node and links [[link]](./balanced-search-trees)

11. **Red-Black Balanced Search Trees**: (data structure) it solves the overhead problem of standard balanced trees. The implementation guarantees O(log N) time complexity in all the operations. The resulting tree is not perfectly balanced in some particular cases [[link]](./red-black-balanced-search-trees)

12. **Geometric applications of BST**: (applications) variations of BSTs can be used in a variety of geometric applications, such as evaluating segment and rectangle intersections. [[link]](./geometric-bst)

13. **Hash tables**: (data structure) using an hash function that maps any integer into a subset it is possible to store a large number of values into a limited number of bins [[link]](./hash-functions)

14. **Graphs**: (data structure) the graph data structure is very important and it can be implemented in three ways. The first way is using a matrix of size V*V where each value identifies a connection between two vertices. The third way is using an adjacency-list, meaning a list of list where for each vertex there is associated a list of neighbours. [[link]](./graph)

15. **Depth-First Search**: (search algorithm) using a depth search it is possible to look for path and vertex in a graph. It can be used to verify in constant time if two nodes are connected. [[link]](./depth-first-search)

16. **Breadth-First Search**: (search algorithm) using a breadth search it is possible to look for path and vertex in a graph. It is used to find the shortest path between two nodes. [[link]](./breadth-first-search)

# Algorithms Part II
------------------

17. **Direct Graphs (Digraphs)**: (data structure) a directed graph or digraph has directed edges. The depth-first and breadth-first algorithms still work. However finding strong connected components requires a slightly more complex algorithm. [[link]](./digraph)

18. **Minimum Spanning Trees**: (data structure and search algorithm) sometimes it is necessary to find the minimum set of edges connecting all the nodes, where to each edge it is associated a weigh. The minimum spanning tree correspond to the tree having the edges with lowest weight connecting all the nodes. Here are discussed three implementations: greedy, Kruskal, and Prim. [[link]](./minimum-spanning-trees)

19. **Shortest path**: (search algorithm) finding the shortest path between two nodes in efficient way is not easy. Here are discussed different solutions and the Dijkstra algorithm [[link]](./shortest-path)

## Useful templates and strategies
---------------------------------

- **Boyer–Moore majority vote**: finding the majority of a sequence of elements using linear time and constant space [[link]](./useful/boyer-moore-majority/README.md)

- **Find loops (an topological sorting) in directed graphs via Depth-First Search**: the use of DFS is the common choice for finding loops and topologically sort a digraph (other choice could be Breadth-First Search) [[link]](./useful/loop-finder-dfs/README.md)

- **Binary search universal template**: a flexible and universal template for solving binary search problems (with examples) [[link]](./useful/template-binary-search/README.md)

- **Divide and Conquer**: Divide and Conquer notes. [[link]](./Divide_And_Conquer)

- **Dynamic Programming**: Dynamic Programming notes. [[link]](./Dynamic_Programming)

- **Backtracking**: Backtracking notes. [[link]](./Backtracking)