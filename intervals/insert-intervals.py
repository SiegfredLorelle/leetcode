"""Insert Interval
You are given an array of non-overlapping intervals intervals 
where intervals[i] = [starti, endi] represent 
the start and the end of the ith interval and 
intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents 
the start and end of another interval.

Two intervals are considered overlapping if they share at least one point.

Insert newInterval into intervals such that intervals is still 
sorted in ascending order by starti and 
intervals still does not have any overlapping intervals 
(merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. 
You can make a new array and return it.
"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        # we go through each intervals, try to merge the new_interval as needed.
        # we update new_interval variable every merge
        for idx, interval in enumerate(intervals):
            # if new_interval is before the first interval OR
            # the rest of intervals are bigger than the new_interval
            if newInterval[1] < intervals[idx][0]:
                res.append(newInterval)
                return res + intervals[idx : ]
            # if new_interval is is bigger than current intervals
            # so we add the current interval and check the next
            elif newInterval[0] > intervals[idx][1]:
                res.append(intervals[idx])

            # merge the current interval and the new_interval
            else:
                newInterval = [
                    min(newInterval[0], intervals[idx][0]),
                    max(newInterval[1], intervals[idx][1]),
                ]

        # the new interval reached the final step
        res.append(newInterval)
        return res

