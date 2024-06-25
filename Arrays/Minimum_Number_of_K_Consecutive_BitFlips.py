# You are given a binary array nums and an integer k.

# A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, 
# and every 1 in the subarray to 0.

# Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

# A subarray is a contiguous part of an array.

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        isFlipped = [0] * n
        flip, flips = 0, 0

        for i in range(n):
            if i >=k:
                flip ^= isFlipped[i-k]
            
            if nums[i] == flip:
                if i + k > n:
                    return -1
                flips += 1
                flip ^= 1
                if i + k < n:
                    isFlipped[i] = 1
        return flips