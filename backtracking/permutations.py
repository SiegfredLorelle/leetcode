from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        currPermutations = []
        def dfs(numsToAdd):
            if not numsToAdd:
                ans.append(currPermutations.copy())
                return
            
            for i, num in enumerate(numsToAdd):
                currPermutations.append(num)
                currNumsToAdd = numsToAdd.copy()
                currNumsToAdd.pop(i)
                dfs(currNumsToAdd)
                currPermutations.pop()

        dfs(nums)
        return ans