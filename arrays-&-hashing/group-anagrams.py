"""
Group Anagrams

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by 
rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """ Solution using sort """

        # sorted word : [words]
        # anagrams = {}

        # for word in strs:
        #     sorted_word = "".join(sorted(word))
        #     if sorted_word in anagrams:
        #         anagrams[sorted_word].append(word)
        #     else:
        #         anagrams[sorted_word] = [word]

        # return anagrams.values()
            


        """ Solution by counting characters """
        from collections import defaultdict

        anagrams = defaultdict(list)

        for word in strs:
            counter = [0] * 26

            for char in word:
                counter[ord(char) - ord("a")] += 1

            anagrams[tuple(counter)].append(word)

        return anagrams.values()




sol = Solution()
result = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)



