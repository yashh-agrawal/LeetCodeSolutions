# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()

        n = len(arr)

        if n%2==0:
            result = float(arr[n//2] + arr[n//2 - 1])/2.0
        else:
            result = float(arr[n//2])
        return result