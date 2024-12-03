from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        currArr = [] 
        print(candidates)
        def dfs(start, total):
            if total == target:
                res.append(currArr.copy())
                return
            for current in range(start, len(candidates)):
                if current != start and candidates[current] == candidates[current - 1]:
                    continue
                if total + candidates[current] > target:
                    break
                
                currArr.append(candidates[current])
                dfs(current + 1, total + candidates[current])
                currArr.pop()

        dfs(0, 0)
        return res

