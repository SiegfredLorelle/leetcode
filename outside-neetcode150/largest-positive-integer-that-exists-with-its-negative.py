""" Largest Positive Integer That Exists With Its Negative

Given an integer array nums that does not contain any zeros, 
find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.
"""
from typing import *

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        posis = set()
        negas = set()
        maxNum = -1

        for num in nums:
            if num > 0:
                if num in negas and num > maxNum:
                    maxNum = num
                posis.add(num)
            else:
                posi_num = -num
                if posi_num in posis and posi_num > maxNum:
                    maxNum = posi_num
                negas.add(posi_num)
        
        return maxNum