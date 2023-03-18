class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in hash:
                return [hash[complement], index]
            else:
                hash[num] = index


sol = Solution()
result = sol.twoSum([2,7,11,15], 9)
print(result)