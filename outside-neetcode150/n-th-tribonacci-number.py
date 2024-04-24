""" N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        seq = deque([0, 1, 1])

        if n < 3:
            return seq[n]

        for _ in range(3, n):
            seq.append(sum(seq))
            seq.popleft()
        
        return sum(seq)