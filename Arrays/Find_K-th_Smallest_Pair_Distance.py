# The distance of a pair of integers a and b is defined as the absolute difference between a and b.

# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        minDist, maxDist = 0, nums[-1] - nums[0]

        while minDist < maxDist:
            midDist = (minDist + maxDist) // 2
            if self.countPairsWithinDistance(nums,midDist) < k:
                minDist = midDist + 1
            else:
                maxDist = midDist
        return minDist

    def countPairsWithinDistance(self, numbers, targetDist):
        count = left = 0
        for right in range(0, len(numbers)):
            while numbers[right] - numbers[left] > targetDist:
                left += 1
            count += right - left
        return count