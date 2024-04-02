# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j=0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j+=1
        return nums
        
        