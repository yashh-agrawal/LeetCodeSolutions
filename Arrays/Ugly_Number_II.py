# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        i2 = i3 = i5 = 0
        ugly = [1]

        while len(ugly) < n:
            
            next_ugly_2 = ugly[i2] * 2
            next_ugly_3 = ugly[i3] * 3
            next_ugly_5 = ugly[i5] * 5

            next_ugly = min(next_ugly_2, next_ugly_3, next_ugly_5)
            ugly.append(next_ugly)

            if next_ugly == next_ugly_2:
                i2 += 1
            if next_ugly == next_ugly_3:
                i3 += 1
            if next_ugly == next_ugly_5:
                i5 += 1
        
        return ugly[-1]