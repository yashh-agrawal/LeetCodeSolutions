# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
# such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i, num in enumerate(nums):
            if num in table and i - table[num] <= k:
                return True
            table[num] = i
        return False
        