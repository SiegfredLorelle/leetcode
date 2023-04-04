"""
Largest Rectangle in Histogram

Given an array of integers heights 
representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.
"""



class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # [ (index, height) ], this can also be called as stack
        uncomputed_rectangles = [] 
        max_area = heights[0]

        for i, height in enumerate(heights):
            start = i
            while uncomputed_rectangles and uncomputed_rectangles[-1][1] > height:
                prev_i, prev_height = uncomputed_rectangles.pop()

                area = prev_height * (i - prev_i)
                if max_area < area:
                    max_area = area
                start = prev_i
                # # Or use python built in max (more readable, but slightly slower)
                # max_area = max(max_area, prev_height * (i - prev_i))

            uncomputed_rectangles.append((start, height)) 

        for i, height in uncomputed_rectangles:
            area = height * (len(heights) - i)
            if area > max_area:
                max_area = area
            # # Or use python built in max (more readable, but slightly slower)
            # max_area = max(max_area, prev_height * height * (len(heights) - i))
            

        return max_area












sol = Solution()
result = sol.largestRectangleArea([2,1,5,6,2,3])
print(result)