""" Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, 
the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, 
she eats all of them instead and 
will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas 
before the guards return.

Return the minimum integer k such that 
she can eat all the bananas within h hours.
"""

from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        MAX = max(piles)
        res = MAX
        
        # Use Binary Search to find the lowest middle (k)
        start, end = 1, MAX
        while start <= end:
            # Solve for the middle
            middle = (start + end) // 2

            # Compute the total hours it take to each all bananas
            total = 0
            for pile in piles:
                total += ceil(pile / middle)
                # If total hours is already more than the given h, 
                # Then it is safe to assume than the middle is not the min k
                if total > h:
                    total = float("inf")
                    break

            # Move the pointers appropriately
            if total <= h:
                if middle < res:
                    res = middle
                end = middle - 1
            else:
                start = middle + 1

        return res


sol = Solution()
result = sol.minEatingSpeed(piles=[3,6,7,11], h=8)
print(result)