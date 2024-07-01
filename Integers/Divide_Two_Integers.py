# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. 
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        sign = -1 if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0) else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = len(range(0, dividend-divisor + 1, divisor))

        if sign == -1:
            result = -result

        minus_limit = -(2 ** 31)
        plus_limit = (2 ** 31 - 1)

        result = min(max(result, minus_limit), plus_limit)
        
        return result