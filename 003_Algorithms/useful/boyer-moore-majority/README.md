

The [Boyer–Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm) is an algorithm for finding the majority of a sequence of elements using linear time and constant space. It is named after Robert S. Boyer and J Strother Moore, who published it in 1981, and is a prototypical example of a [streaming algorithm](https://en.wikipedia.org/wiki/Streaming_algorithm). Streaming algorithms are algorithms for processing data streams in which the input is presented as a sequence of items and can be examined in only a few passes (typically just one). In most models, these algorithms have access to limited memory (generally logarithmic in the size of and/or the maximum value in the stream). They may also have limited processing time per item.

In its simplest form, the algorithm finds a **majority element**, if there is one: that is, an element that occurs repeatedly for more than half of the elements of the input. A version of the algorithm that makes a second pass through the data can be used to verify that the element found in the first pass really is a majority. If a second pass is not performed and there is no majority the algorithm will not detect that no majority exists.

**Correctness**: if there is a majority element, the algorithm will always find it. For, supposing that the majority element is `m`, let `c` be a number defined at any step of the algorithm to be either the counter, if the stored element is `m`, or the negation of the counter otherwise. Then at each step in which the algorithm encounters a value equal to `m`, the value of `c` will increase by one, and at each step at which it encounters a different value, the value of `c` may either increase or decrease by one. If `m` truly is the majority, there will be more increases than decreases, and `c` will be positive at the end of the algorithm. But this can be true only when the final stored element is `m`, the majority element. 

Implementation
--------------

The algorithm maintains in its local variables a sequence element and a counter, with the counter initially zero. It then processes the elements of the sequence, one at a time. When processing an element `x`, if the counter is zero, the algorithm stores `x` as its remembered sequence element and sets the counter to one. Otherwise, it compares `x` to the stored element and either increments the counter (if they are equal) or decrements the counter (otherwise). At the end of this process, if the sequence has a majority, it will be the element stored by the algorithm.


Example
--------

**Question**: Leetcode question (easy). Given an array of size `n`, find the majority element. The majority element is the element that appears more than `n/2` times. You may assume that the array is non-empty and the majority element always exist in the array. 

```
Input: [2,2,1,1,1,2,2]
Output: 2
```

**Solution**:

```python
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
```
Essentially, what Boyer-Moore does is look for a suffix `suf` of `nums` where `suf[0]` is the majority element in that suffix. To do this, we maintain a `count`, which is incremented whenever we see an instance of our current candidate for majority element and decremented whenever we see anything else. Whenever `count==0`, we effectively forget about everything in `nums` up to the current index and consider the current number as the candidate for majority element. It is not immediately obvious why we can get away with forgetting prefixes of `nums` consider the following examples (pipes are inserted to separate runs of nonzero count).

`[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]`

Here, the 7 at index 0 is selected to be the first candidate for majority element. count will eventually reach 0 after index 5 is processed, so the 5 at index 6 will be the next candidate. In this case, 7 is the true majority element, so by disregarding this prefix, we are ignoring an equal number of majority and minority elements. It follows that 7 will still be the majority element in the suffix formed by throwing away the first prefix.

`[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 5, 5, 5, 5]`

Now, the majority element is 5 (we changed the last run of the array from 7s to 5s), but our first candidate is still 7. In this case, our candidate is not the true majority element, but we still cannot discard more majority elements than minority elements (this would imply that count could reach -1 before we reassign candidate, which is obviously false).

Therefore, given that it is impossible (in both cases) to discard more majority elements than minority elements, we are safe in discarding the prefix and attempting to recursively solve the majority element problem for the suffix. Eventually, a suffix will be found for which count does not hit 0, and the majority element of that suffix will necessarily be the same as the majority element of the overall array.

Material
--------
