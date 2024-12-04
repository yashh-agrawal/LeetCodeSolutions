# You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.

# You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:

# Choose one integer x from either the start or the end of the array nums.
# Add multipliers[i] * x to your score.
# Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
# Remove x from nums.
# Return the maximum score after performing m operations.

class Solution:
    def maximumScore(self, nums: List[int], muls: List[int]) -> int:
        n, m = len(nums), len(muls)
        
        @lru_cache(2000)
        def dp(l, i):
            if i == m: return 0
            pickLeft = dp(l+1, i+1) + nums[l] * muls[i]
            pickRight = dp(l, i+1) + nums[n-(i-l)-1] * muls[i]
            return max(pickLeft, pickRight)
        
        return dp(0, 0)