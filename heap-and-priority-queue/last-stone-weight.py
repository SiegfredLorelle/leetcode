""" Last Stone Weight
You are given an array of integers stones where stones[i] 
is the weight of the ith stone.

We are playing a game with the stones. 
On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. 
The result of this smash is:

- If x == y, both stones are destroyed, and
- If x != y, the stone of weight x is destroyed, 
    and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. 
If there are no stones left, return 0.
"""

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        
        # Build max heap comprising ofstones
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        # Smash biggest and 2nd biggest stones, then add the new stone
        while len(maxHeap) > 1:
            biggestStone1st = heapq.heappop(maxHeap)
            biggestStone2nd = heapq.heappop(maxHeap)
            
            if biggestStone1st < biggestStone2nd:
                heapq.heappush(maxHeap, biggestStone1st - biggestStone2nd)

        # Return last remaining stone
        if not maxHeap:
            return 0
        return -maxHeap[0]