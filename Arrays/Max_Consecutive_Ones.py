# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        temp =0
        for i in nums:
            if i == 1:
                temp +=1 
            else:
                count = max(count, temp)
                temp = 0
        return max(count,temp)