# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

#Approach 1:

class Solution:
    def mySqrt(self, x: int) -> int:
        result = []
        for i in range(0,x-1):
            if i*i<=x:
                result.append(i)
            else:
                break
        print(result)
        return result[-1]
    

#Approach 2: Binary Search
    
    class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        first, last = 1, x

        while first <= last:
            mid = first + ((last - first) // 2)

            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            elif mid < x // mid:
                first = mid + 1
        return last
