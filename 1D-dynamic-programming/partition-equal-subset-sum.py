from types import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total / 2

        mem = set([0])

        for num in nums:
            for mem_num in set(mem):
                new_num = num + mem_num
                if new_num == target:
                    return True
                if new_num > target:
                    continue
                mem.add(num)
                mem.add(new_num)

        return False

