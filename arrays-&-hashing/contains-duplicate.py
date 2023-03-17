class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False





sol = Solution()
result = sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(result)