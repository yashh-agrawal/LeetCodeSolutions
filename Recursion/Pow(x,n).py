# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = -n

        power = 1
        cur_prod = x
        while n > 0:
            if n%2:
                power = power * cur_prod
            cur_prod = cur_prod * cur_prod
            n = n//2
        return power

#Approach 2
    
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def power(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return power(base * base, exponent // 2)
            else:
                return base * power(base*base, (exponent -1 ) // 2)
        p = power()

        return float(p) if n >=0 else 1/p