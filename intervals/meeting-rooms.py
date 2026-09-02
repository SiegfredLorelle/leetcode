"""Meeting Rooms

Given an array of meeting time interval objects 
consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
determine if a person could add all meetings to 
their schedule without any conflicts. 
The intervals may be provided in any order.

Note: (0,8),(8,10) is not considered a conflict at 8
"""

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from type import List

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True

        intervals.sort(
            key=lambda interval: interval.start, 
            reverse=False
        )

        prev_end = intervals[0].end
        for curr in intervals[1 : ]:
            if prev_end > curr.start:
                return False
            prev_end = curr.end

        return True

