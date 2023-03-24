""" 
Encode and Decode Strings

Design an algorithm to encode a list of strings to a string.

The encoded string is then sent over the network and
is decoded back to the original list of strings.

Please implement encode and decode
"""


class Solution:
    """ UNTESTED CODE """

    
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
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here

        strs = []
        word_length = ""
        i = 0
        while True:
            if str[i].is_digit():
                word_length += str[i]

                if str[i + 1] == ":":
                    word = ""
                    i += 2
                    for j in str[i: i + word_length]:
                        word += j
                    strs.append(word)
                    i += word_length

        return strs


sol = Solution()
encode_result = sol.encode(["we", "say", ":", "yes"])
decode_result = sol.decode(encode_result)
print(decode_result)