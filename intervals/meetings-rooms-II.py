"""Meeting Rooms II
Given an array of meeting time interval objects consisting of 
start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
find the minimum number of rooms required to 
schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.
"""

from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        starts = []
        ends = []

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        starts.sort()
        ends.sort()

        start_idx = 0
        end_idx = 0
        active_rooms_count = 0
        res = 0
        while start_idx < len(intervals):
            if starts[start_idx] < ends[end_idx]:
                start_idx += 1
                active_rooms_count += 1
            else:
                end_idx += 1
                active_rooms_count -= 1
            res = max(res, active_rooms_count)

        return res

