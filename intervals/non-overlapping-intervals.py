"""Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals 
you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. 
For example, [1, 2] and [2, 3] are non-overlapping.
"""

from type import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0], reverse=False)

        res = 0
        prev_end = intervals[0][1]

        for curr_start, curr_end in intervals[1 : ]:
            if prev_end <= curr_start:
                prev_end = curr_end
            else:
                prev_end = min(prev_end, curr_end)
                res += 1

        return res

