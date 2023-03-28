"""
Trapping Rain Water

Given n non-negative integers representing
an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""

class Solution:
    def trap(self, height: list[int]) -> int:

        if len(height) <= 2:
            return 0

        total_trapped_area = 0
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]

        while l < r:
            if max_left < max_right:
                l += 1

                if max_left < height[l]:
                    max_left = height[l]
                else:
                    trapped_area = max_left - height[l] 
                    if trapped_area > 0:
                        total_trapped_area += trapped_area
                
                # # OR USE MAX BUILT-IN FUNC (SLIGHTLY SLOWER BUT MORE READABLE)
                # max_left = max(max_left, height[l])
                # total_trapped_area += max_left - height[l]

            else:
                r -= 1
                if max_right <= height[r]:
                    max_right = height[r]
                else:
                    trapped_area = max_right - height[r] 
                    if  trapped_area > 0:
                        total_trapped_area += trapped_area  
                # # OR USE MAX BUILT-IN FUNC (SLIGHTLY SLOWER BUT MORE READABLE)
                # max_right = max(max_right, height[r])
                # total_trapped_area += max_right - height[r]

        return total_trapped_area


sol = Solution()
result = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(result)