# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls 
# if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], 
# Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force 
# between any two balls is maximum.

# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

# Given the integer array position and the integer m. Return the required force.

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            last_position, balls = position[0], 1
            for i in range(1, len(position)):
                if position[i] - last_position >= mid:
                    last_position = position[i]
                    balls += 1
            if balls >= m:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans