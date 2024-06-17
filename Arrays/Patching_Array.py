# Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] 
# inclusive can be formed by the sum of some elements in the array.

# Return the minimum number of patches required.

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        currentSum = 1
        patches = 0
        index = 0

        while currentSum <= n:
            if index < len(nums) and nums[index] <= currentSum:
                currentSum += nums[index]
                index += 1
            else:
                currentSum += currentSum
                patches += 1
        return patches