# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c))+1):
            j = sqrt(c - i * i)
            if j == int(j):
                return True
        return False