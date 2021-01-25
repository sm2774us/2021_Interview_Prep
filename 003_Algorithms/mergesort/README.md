
The [mergesort](https://en.wikipedia.org/wiki/Merge_sort) is a divide-and-conquer sorting algorithm invented by John Von Neumann in 1945. The first step of the algorithm consists in dividing the list in *n* sublists (each containing 1 element). The second step consists in merging the sublists producing new sublists with more elements. The process finishes when only 1 sublist remains. As the name suggest there are two main methods in this algorithm, the method `merge()` and the method `sort()`. The input is an array `a[]` containing comparable elements. An auxiliary array called `aux[]` is used in order to store the temporary ordered elements. The algorithm has N*log(N) complexity because divides the array to sort in sub-arrays reducig (or increasing) the size by power of 2. Moreover this complexity is kept also in the worst case, while other algorithms such as quicksort does not have this property.
Mergesort is not only efficient but also **stable**. The stability of a sorting algorithm is the ability of preserving order when sort by different criteria. For example sorting by name and then by place, a not stable algoritm will loose the first sorting when the second is applied.
Finally mergesort is highly parallelizable using the Three Hungarians' Algorithm.


Implementation
--------------

1. **Top-Down:**  A `mid` point variable is estimated dividing the input array in half. The half is then divided in half, and so on. The last couple of elements are sorted.

2. **Bottom-Up:** Starting only from two values is applied the `merge()` method. A step is done on the original array and the next couple is considered for merging. When all the couples are exausted then 4 elements are merged. When the 4 elements are exausted then it is necessary to look for 8 elements. The size of the arrays considered is doubled every time (N log(N) complexity)


Methods
--------

- `merge()`: it merges two halves moving on them and selecting the smallest element
- `sort()`: it sorts the input array

Applications
------------

1. Sorting a list of numbers
2. Sort a list of music songs by name
3. Sort polar coordinates of points in a polar plot

Quiz
-----

1. Merging with smaller auxiliary array. Suppose that the subarray `a[0]` to `a[n−1]` is sorted and the subarray `a[n]` to `a[2*n−1]` is sorted. How can you merge the two subarrays so that `a[0]` to `a[2*n−1]` is sorted using an auxiliary array of length `n` (instead of `2n`)?

2. Counting inversions. An inversion in an array `a[]` is a pair of entries `a[i]` and `a[j]` such that `i<j` but `a[i]>a[j]`. Given an array, design a linearithmic algorithm to count the number of inversions.

Material
--------
- **Coursera Algorithms Part 1**: week 3
- **Algorithms**, Sedgewick and Wayne (2014): Chapter 2.2
