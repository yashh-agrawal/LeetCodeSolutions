# Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        flip , wflip = 0, 0
        maxx= 0

        for i,v in enumerate(nums):
            if v == 1:
                flip += 1
                wflip += 1
            else:
                flip = wflip+1
                wflip = 0
            maxx = max(maxx, flip, wflip)
        return maxx       