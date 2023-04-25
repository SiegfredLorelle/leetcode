"""Sliding Window Maximum

You are given an array of integers nums, 
there is a sliding window of size k 
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Return the max sliding window.
"""

import collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_queue = collections.deque()
        start_index = 0
        max_sliding_window = []

        for i, num in enumerate(nums, 1):
            while max_queue and max_queue[-1] < num:
                max_queue.pop()
            max_queue.append(num)

            if i >= k:
                max_sliding_window.append(max_queue[0])
                if max_queue[0] == nums[start_index]:
                    max_queue.popleft()
                start_index += 1

        return max_sliding_window


sol = Solution()
result = sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
print(result)