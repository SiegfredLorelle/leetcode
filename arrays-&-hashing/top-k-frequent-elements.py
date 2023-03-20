"""
Top K Frequent Elements
Given an integer array nums and an integer k, 
return the k most frequent elements. 

You may return the answer in any order.
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # # SOLUTION USING SORT FUNCTION
        # hashmap = {}

        # for num in nums:
        #     if num not in hashmap:
        #         hashmap[num] = 1
        #     else:
        #         hashmap[num] += 1

        # hashmap = dict(sorted(hashmap.items(), reverse=True, key=lambda x : x[1]))

        # return [num for i, num in enumerate(hashmap) if i < k]
        # # OR RETURN ASAP BY USING FOR LOOP
        # for index, num in enumerate(hashmap, start=1):
        #     result.append(num)
        #     if index == k:
        #         return result


        # # SOLUTION USING BUCKET SORT
        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Count the frequency via hashmaps
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        # Append the num in the index of its frequency
        for key, value in hashmap.items():
            freq[value].append(key)
        
        # Fill up the res by looping through freq in reverse until
        # size of res is k
        res = []
        for index in range(len(freq) - 1, 0, -1):
            for i in freq[index]:
                res.append(i)
                if len(res) == k:
                    return res




sol = Solution()
result = sol.topKFrequent([1,1,1,2,2,3], 2)
print(result)