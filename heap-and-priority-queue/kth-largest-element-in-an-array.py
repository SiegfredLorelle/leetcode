"""Kth Largest Element in an Array
Given an integer array nums and an integer k, 
return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Can you solve it without sorting?
"""
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, -num)

        for _ in range(k - 1):
            heapq.heappop(maxHeap)
        return -maxHeap[0]