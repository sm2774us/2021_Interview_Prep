# Intervals
- https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%8C%BA%E9%97%B4%E8%B0%83%E5%BA%A6%E9%97%AE%E9%A2%98%E4%B9%8B%E5%8C%BA%E9%97%B4%E5%90%88%E5%B9%B6.md
- https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%8C%BA%E9%97%B4%E4%BA%A4%E9%9B%86%E9%97%AE%E9%A2%98.md 

## 0) Concept  

### 0-1) Framework
- Merge intervals
- Overlap intervals
- Courses problems
- Meeting room problems

### 0-2) Pattern
```python
# python
def intervalsPattern(points):
    if not points: return 0
    points.sort(key = lambda x : x[1]) # or points.sort(key = lambda x : x[0])...depends  
    curr_pos = points[0][1]
    ans = 1
    for i in range(len(points)):

        if some_condition:
            # do sth
        else:
            # do sth
    return ans
```

## 1) General form

### 1-1) Basic OP

## 2) LC Example

### 2-1) Non-overlapping Intervals
```python
# 435 Non-overlapping Intervals
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals: return 0
        intervals.sort(key = lambda x : x[0])
        last = 0
        res = 0
        for i in range(1, len(intervals)):
            if intervals[last][1] > intervals[i][0]:
                if intervals[i][1] < intervals[last][1]:
                    last = i
                res += 1
            else:
                last = i
        return res
```

### 2-2) Minimum Number of Arrows to Burst Balloons
```python
# 452 Minimum Number of Arrows to Burst Balloons
# https://blog.csdn.net/MebiuW/article/details/53096708
class Solution(object):
    def findMinArrowShots(self, points):
        if not points: return 0
        points.sort(key = lambda x : x[1])
        curr_pos = points[0][1]
        ans = 1
        for i in range(len(points)):
            if curr_pos >= points[i][0]:
                continue
            curr_pos = points[i][1]
            ans += 1
        return ans
```
