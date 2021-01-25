
Definition: the [Priority-Queue](https://en.wikipedia.org/wiki/Priority_queue) data structure associates a key to a value. An appropriate data type in such an environment supports two operations: remove the maximum and insert. Such a data type is called a priority queue. Using priority queues is similar to using queues (remove the oldest) and stacks (remove the newest), but implementing them efficiently is more challenging.


Implementation
--------------

1. **Ordered array**: based on an array of ordered values that is adjusted every time a new element is inserted. For instance starting from the array `[45, 49, 68, 89]` if we push a new element `54` we have to find the place where it must be inserted and this can be done using a *insertion sort* like mechanism and the method `less()`. In our example the element can be added to the end of the cue and then using the method `less()` compared with the element on the left, the two elements are switched until `less()` returns true. For instance starting from `[45, 49, 68, 89, 54]` we perform `less(89, 54) -> False` and switch the last two elements in this way `[45, 49, 68, 54, 89]` then we compare again `less(68, 54) -> False` and switch in this way `[45, 49, 54, 68, 89]`, finally we get `less(68, 54) -> True` meaning that we reached the correct position. The complexity of this method in the worst case is O(N) for insertion, but since the array is ordered it takes only O(1) to return the largest element (the last one in the array).

2. **Unordered array**: this is the lazy approach. The array of value is kept unordered and a new element is added at the end. Differently from the ordered solution, here adding a new element is very easy and only takes O(1) time complexity. The problem comes when we have to find the largest element, because this operation takes O(N) time complexity requiring to scan the entire array. 

3. [binary heap](https://en.wikipedia.org/wiki/Binary_heap): using this data structure it is possible to obtain a complexity of O(log N) for both insertion and max element return. The binary heap is a tree where *each node has only two children* that are smaller than the parent. The root node of the tree is the largest element in the set. The elements are stored into an array, each parent at index `k` has two children at index `2k` and `2k+1` (on the opposite each child in position `k` has a parent in position `k/2`).
To use the binary heap we have to implement two operations needed for restoring the heap order (reheapify): top-down (sink), bottom-up (swim). The **top-down** operation is used when a node key becomes smaller than one (or both) of the children's key. What is done is to use a switching mechanism similar to the *insertion sort* were we exchange parent-child until the correct order is obtained. The top-down is used when the `delMax()` method is called. The root is removed and the smallest element at the end of the array is moved at the top, then the sink is called and the order restored.
On the other hand the **bottom-up** operation proceed in the reverse order. If a child got a priority that is higher than the parent it is necessary to exchange child-parent until the correct order is obtained. The bottom-up is used when the `insert()` is called and a new element is added to the array. The element is added in the last position in the array and the swim is performed to reorder the tree.


Methods
--------

`delMax()`: remove the element with the largest priority and returns it

`insert()`: a new element in the queue

`less()`: compares two elements and returns a boolean

`sink()`: (binary heap) implement the top-down reordering of the nodes

`swim()`: (binary heap) implement the bottom-up reordering of the nodes

Applications
------------

1. System processes priority management. Smartphone application priority (e.g. a phone call has higher priority than a game)


Quiz
-----




Material
--------
- **Coursera Algorithms Part 1**: week 4
- **Algorithms**, Sedgewick and Wayne (2014): Chapter 2.4 "Priority Queues"


