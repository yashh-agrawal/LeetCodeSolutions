# Given an integer array nums, return the third distinct maximum number in this array. 
# If the third maximum does not exist, return the maximum number.
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = list(set(nums))
        l.sort()
        if len(l)>=3:
            return l[len(l)-3]
        else:
            return max(l)
        