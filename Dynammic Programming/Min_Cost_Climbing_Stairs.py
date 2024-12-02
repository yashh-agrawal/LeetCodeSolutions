# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i):
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            if i not in memo:
                memo[i] = cost[i] + min(dp(i - 1), dp(i - 2))
            return memo[i]
        memo = {}
        n = len(cost)
        return min(dp(n - 1), dp(n - 2))