""" 
Encode and Decode Strings

Design an algorithm to encode a list of strings to a string.

The encoded string is then sent over the network and
is decoded back to the original list of strings.

Please implement encode and decode
"""


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for word in strs:
            res += f"{len(word)}:{word}"
        return res


    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        i = 0 # char pointer
        j = 0 # word length pointer

        while i < len(str):
            if str[i] != ":":
                i += 1

            else:
                word_length = int(str[j : i])
                res.append(str[i + 1 : i + 1 + word_length])
                i += word_length + 1
                j = i
        return res




sol = Solution()
encode_result = sol.encode(["we", "say", ":", "yes"])
decode_result = sol.decode(encode_result)
print(decode_result)