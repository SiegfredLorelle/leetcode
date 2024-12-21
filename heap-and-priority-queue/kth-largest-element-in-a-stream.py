"""Kth Largest Element in a Stream
You are part of a university admissions office and 
need to keep track of the kth highest test score from applicants in real-time. 
This helps to determine cut-off marks for 
interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, 
maintains a stream of test scores and continuously returns the 
kth highest test score after a new score has been submitted. 
More specifically, we are looking for 
the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

- KthLargest(int k, int[] nums) Initializes the object with the integer k 
    and the stream of test scores nums.
- int add(int val) Adds a new test score val to the stream 
    and returns the element representing the 
    kth largest element in the pool of test scores so far.
"""

from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        
        # Build min heap of size k
        for num in nums:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add element in min heap
        heapq.heappush(self.minHeap, val)
        # Pop min heap if its size bigger than k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
