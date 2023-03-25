"""
Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers
that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where
1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must use only constant extra space.
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """ SOLUTION USING HASHMAP """
        # number_hash = {}

        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     if diff in number_hash:
        #         return [number_hash[diff] + 1, i + 1]
        #     number_hash[numbers[i]] = i 






        """ SOLUTION USING TWO POINTERS """
        l = 0
        r = len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [l + 1, r + 1]



sol = Solution()
result = sol.twoSum([2,7,11,15], 9)
print(result)