# A distinct string is a string that is present only once in an array.

# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hmap = {}
        for i in arr:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1
        
        distinct_count = 0
        for i in arr:
            if hmap[i] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return i
        return ""