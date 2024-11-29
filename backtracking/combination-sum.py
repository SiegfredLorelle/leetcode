from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        currCandidates = []
        
        def dfs(i, total):
            if total == target:
                res.append(currCandidates.copy())
                return
            if i >= len(candidates) or total > target:
                return

            currCandidates.append(candidates[i])
            dfs(i, total + candidates[i])
            currCandidates.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res