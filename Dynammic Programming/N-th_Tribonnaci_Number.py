# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

class Solution:
    def tribonacci(self, n: int) -> int:
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 1
            if i not in memo:
                memo[i] = dp(i-1) + dp(i-2) + dp(i-3)
            return memo[i]
        memo = {}
        return dp(n)