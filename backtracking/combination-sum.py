
"""Combination Sum
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates 
where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency 
of at least one of the chosen numbers is different.

The test cases are generated such that the number 
of unique combinations 
that sum up to target is less than 150 combinations for the given input.
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """ 
        SOLUTION USING DECISION TREE TO EITHER INCLUDE OR EXCLUDE CANDIDATE 
        """
        # res = []
        # currCandidates = []
        
        # def dfs(i, total):
        #     if total == target:
        #         res.append(currCandidates.copy())
        #         return
        #     if i >= len(candidates) or total > target:
        #         return

        #     currCandidates.append(candidates[i])
        #     dfs(i, total + candidates[i])
        #     currCandidates.pop()
        #     dfs(i + 1, total)

        # dfs(0, 0)
        # return res

        """ 
        SOLUTION USING DECISION TREE TO EXPLORE ALL POSSIBLE COMBINATIONS
        """
        candidates.sort()
        res = []
        currCombination = []

        def dfs(i, currSum):
            if currSum == target:
                res.append(currCombination.copy())
                return
            if i >= len(candidates):
                return

            for j in range(i, len(candidates)):
                if currSum + candidates[j] > target:
                    break
                currCombination.append(candidates[j])
                dfs(j, currSum + candidates[j])
                currCombination.pop()

        dfs(0, 0)
        return res