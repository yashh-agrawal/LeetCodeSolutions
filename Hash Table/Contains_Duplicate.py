# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.Given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        for i in nums:
            if i in hs:
                return True
            hs.add(i)
        return False
        