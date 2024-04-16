# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hs = set(nums1)
        intersection = []
        for num in nums2:
            if num in hs:
                intersection.append(num)
                hs.remove(num)
        return intersection
