"""K Closest Points to Origin
Given an array of points where points[i] = [xi, yi] 
represents a point on the X-Y plane and 
an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance 
(i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. 
The answer is guaranteed to be unique (except for the order that it is in).
"""

from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    """ SOLUTION USING SORT """
    # points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
    # return points[:k]

    """ SOLUTION USING MAX HEAP """
        maxHeap = []
        for point in points:
            x, y = point
            distance = x ** 2 + y ** 2
            heapq.heappush(maxHeap, (-distance, x, y))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [[x, y] for _, x, y in maxHeap]