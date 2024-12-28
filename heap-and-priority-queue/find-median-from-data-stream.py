"""Find Median from Data Stream
The median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value, 
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
- void addNum(int num) 
    adds the integer num from the data stream to the data structure.
- double findMedian() 
    returns the median of all elements so far. 
    Answers within 10-5 of the actual answer will be accepted.
"""

import heapq

class MedianFinder:
    """
    The numbers are divided into two halves:
        - A smaller half, managed as a Max Heap (`smallHalf`)
        - A larger half, managed as a Min Heap (`bigHalf`)
    
    Properties:
        - All numbers in `smallHalf` are less than or equal to all numbers in `bigHalf`.
        - The median is determined as follows:
            1. If the sizes of the two heaps differ, the median is the root of the larger heap.
            2. If the sizes of the two heaps are equal, the median is the mean of the two roots:
                - The maximum of `smallHalf`
                - The minimum of `bigHalf`
    """
    def __init__(self):
        self.smallHalf = [] # Max Heap
        self.bigHalf = [] # Min Heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHalf, -num)
        
        # Rebalance heaps if size of `smallHalf` is much larger than `bigHalf`
        while abs(len(self.smallHalf) - len(self.bigHalf)) > 1:
            midSmall = -heapq.heappop(self.smallHalf)
            heapq.heappush(self.bigHalf, midSmall)

        # Ensures all element in `smallHalf` are less than `bigHalf` 
        while self.bigHalf and -self.smallHalf[0] > self.bigHalf[0]:
            midSmall = -heapq.heappop(self.smallHalf)
            heapq.heappush(self.bigHalf, midSmall)
        
        # Rebalance heaps if size of `smallHalf` is much smaller than `bigHalf`
        while abs(len(self.smallHalf) - len(self.bigHalf)) > 1:
            midBig = heapq.heappop(self.bigHalf)
            heapq.heappush(self.smallHalf, -midBig)

    def findMedian(self) -> float:
        # If `smallHalf` has more elements, the median is its maximum
        if len(self.smallHalf) > len(self.bigHalf):
            return -self.smallHalf[0]
        # If `bigHalf` has more elements, the median is its minimum
        if len(self.smallHalf) < len(self.bigHalf):
            return self.bigHalf[0]
        # If both heaps are of equal size, return the mean of the two roots
        return (-self.smallHalf[0] + self.bigHalf[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()