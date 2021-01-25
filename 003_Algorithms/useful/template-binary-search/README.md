
This has been adapted from [this post on leetcode](https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems).

Even if the intuition behind binary-search is simple to grasp, there may be a number of problems when we do a real implementaiton. Some of most common problems include:

- **Exit condition.** When to exit the loop? Should we use `left < right` or `left <= right` as the while loop condition?
- **Boundary init.** How to initialize the boundary variable `left` and `right`?
- **Boundary update.** How to choose from `left = mid`, `left = mid + 1` and `right = mid`, `right = mid - 1`?


Implementation
--------------

We only need to modify three parts after copy-pasting this template, without worrying about corner cases and bugs:

1. Initialize the **boundary variables** `left` and `right` to specify search space (set up the boundary to include all possible elements).
2. Decide **return value**. Is it return `left` or return `left-1`? Remember this: after exiting the while loop, `left` is the minimal `k​` satisfying the condition function.
3. Design the **condition function**.


```python
def binary_search(array) -> int:

    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right: # -> Note the exit condition
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

Example 1
--------

**Question:** You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad. You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API. The following is an example:

```
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
```

**Reasoning:** it is not difficult to see that this could be solved using binary search. Let us see how the search space could be halved each time. Let us look at the **scenario #1** where `isBadVersion(mid)=>false`. We know that all versions preceding and including `mid` are all good. So we set `left=mid+1` to indicate that the new search space is the interval `[mid+1,right]` (inclusive).

```
Scenario #1: isBadVersion(mid) => false

 1 2 3 4 5 6 7 8 9
 G G G G G G B B B       G = Good, B = Bad
 |       |       |
left    mid    right
```

The second possible scenario **scenario #2** (the only scenario left) is where `isBadVersion(mid)=>true`. This tells us that `mid` may or may not be the first bad version, but we can tell for sure that all versions after `mid` can be discarded. Therefore we set `right=mid` as the new search space of interval `[left,mid]` (inclusive).

```
Scenario #2: isBadVersion(mid) => true

 1 2 3 4 5 6 7 8 9
 G G G B B B B B B       G = Good, B = Bad
 |       |       |
left    mid    right
```

How about the **exit condition**? We could guess that `left` and `right` eventually both meet and it must be the first bad version, but how could you tell for sure? This can be [proven by induction](http://www.cs.cornell.edu/courses/cs211/2006sp/Lectures/L06-Induction/binary_search.html), which you can read up yourself if interested. Here is a helpful tip to quickly prove the correctness of your binary search algorithm during an interview. We just need to test an input of size 2. Check if it reduces the search space to a single element (which must be the answer) for both of the scenarios above. If not, your algorithm will never terminate.

Checking for **overflow**. If you are setting `mid=(left+right)/2​`, you have to be very careful. Unless you are using a language that does not overflow such as Python, this could overflow. One way to fix this is to use `left+(right-left)/2`​ instead.

**Solution:** it is possible to use the template straight away for this example. The `isBadVersion()` function can be considered as our condition. The initialization of `left` and `right` should be in the range `[1,n]`. If you fall into this subtle overflow bug, you are not alone. Even Jon Bentley's own implementation of binary search had this overflow bug and remained undetected for over twenty years.

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ## Using the Binary-search template
        #def condition(value) -> bool:
        #pass
        # the condition is already given by isBadVersion
        
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
```


Example 2
----------

**Question:** Implement int `sqrt(int x)`. Compute and return the square root of `x`, where `x` is guaranteed to be a non-negative integer. Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

```
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
```

**Solution:** it is possible to use the template with minimal adjustments for this example. The condition is given by `mid**2>x`, if the integer is greater than our target we move on the left side of the search space by adjusting the `right` boundary (and viceversa). Particular attention is necessary in defining the `right` boundary since the problem ask for a truncation of the decimals irrespective of flooring or ceiling. To solve the issue we have to add an element to the range and define `righ=x+1` as boundary, then subtract a value from the `left` boundary on return.

```python
class Solution:
    def mySqrt(self, x: int) -> int:
    
        def condition(x, mid):
            if(mid**2>x): return True
            else: return False
                   
        left, right = 0, x+1
        while left<right:
            mid=left+(right-left)//2
            if(condition(x,mid)):
                right=mid
            else:
                left=mid+1
        return left-1
```


Example 3
----------

**Question:** given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array.

```
Input: [1,3,5,6], 5
Output: 2
Input: [1,3,5,6], 2
Output: 1
Input: [1,3,5,6], 7
Output: 4
Input: [1,3,5,6], 0
Output: 0
```

**Solution:** also in this case our template is effective and requires minimal adjustments.  The input target might be larger than all elements in `nums` and therefore needs to placed at the end of the array. That's why we should initialize `right = len(nums)` instead of `right = len(nums) - 1`.

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def condition(mid, target):
            if(mid>=target): return True
            else: return False
            
        left, right = 0, len(nums)
        while left<right:
            mid = left + (right-left)//2
            if(condition(nums[mid], target)):
                right=mid
            else:
                left=mid+1
        return left
```

Material
--------
