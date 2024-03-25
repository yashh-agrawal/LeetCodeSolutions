# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = [nums[0]]
        for i in range(1,len(nums)):
            a.append(a[i-1]+nums[i])
        return a