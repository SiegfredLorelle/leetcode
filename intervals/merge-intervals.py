"""Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and 
return an array of the non-overlapping intervals 
that cover all the intervals in the input.
"""

from type import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key=lambda interval : interval[0])
        prev_interval = intervals[0]

        for curr_interval in intervals:
            if prev_interval[1] < curr_interval[0]:
                res.append(prev_interval)
                prev_interval = curr_interval
            else:
                prev_interval = [
                    min(prev_interval[0], curr_interval[0]),
                    max(prev_interval[1], curr_interval[1]),
                ]

        res.append(prev_interval)
        return res

