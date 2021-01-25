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

# Graphing

## Greedy 

### Kruskal's Algorithm

**When to Use:**

*

**Complexity:**

<br/>

### Prim's Algorithm

**When to Use:**

*

**Complexity:**

<br/>

## Dynamic Programming

### Bellman-Ford Algorithm

**When to Use:**

*

**Complexity:**

<br/>

### Dijkstra's Algorithm

**When to Use:**

*

**Complexity:**

<br/>

### A* Search Algorithm

**When to Use:**

*

**Complexity:**

<br/>

## Breadth First Search

**When to Use:**

*

**Complexity:**

<br />

## Depth First Search

**When to Use:**

*

**Complexity:**