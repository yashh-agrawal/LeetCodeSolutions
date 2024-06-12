# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
#  with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

#Approach 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1],nums[j]
        return nums
    
#Approach 2

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) -1

        while mid<=high:
            if nums[mid]==0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1