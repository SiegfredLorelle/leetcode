"""Minimum Interval to Include Each Query

You are given a 2D integer array intervals, 
where intervals[i] = [lefti, righti] 
describes the ith interval starting at lefti and ending at righti (inclusive). 
The size of an interval is defined as the number of integers it contains, 
or more formally righti - lefti + 1.

You are also given an integer array queries. 
The answer to the jth query is the size of the smallest interval i 
such that lefti <= queries[j] <= righti. 
If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.
"""

from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort both intervals and queries.
        # Utilize sorted ordering for adding/removing active intervals
        # Use min heap to keep track of smallest sizes (res)

        import heapq

        intervals.sort(
            key=lambda interval: interval[0],
            reverse=False
        )

        min_heap = []
        heapq.heapify(min_heap)


        size_per_query = {}
        interval_idx = 0
        for query in sorted(queries):
            while interval_idx < len(intervals):
                if intervals[interval_idx][0] > query:
                    break
                left, right = intervals[interval_idx]
                size = right - left + 1
                heapq.heappush(min_heap, (size, right))
                interval_idx += 1


            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)


            if not min_heap:
                size_per_query[query] = -1
            else:
                size_per_query[query] = min_heap[0][0]


        res = []
        for query in queries:
            size = size_per_query[query]
            res.append(size)

        return res

