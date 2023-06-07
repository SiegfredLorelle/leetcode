"""
Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the 
previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity."""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        # row in matrix where the target is within range 
        arr = None 

        # Find the array (row) where the target is within range
        while start <= end:
            middle =  (start + end) // 2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                arr = matrix[middle]
                break
            elif matrix[middle][0] > target:
                end = middle - 1
            else:
                start = middle + 1

        # If array is not found, then target is probably greater than highest 
        # number or lower than the lowest number
        if not arr:
            return False

        start = 0
        end = len(arr) - 1
        
        # Find the target in the array
        while start <= end:
            middle = (start + end) // 2
            if arr[middle] == target:
                return True
            elif arr[middle] > target:
                end = middle - 1
            else:
                start = middle + 1

        return False


sol = Solution()
result = sol.searchMatrix(
    matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 
    target=3
)
print(result)