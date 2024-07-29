# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        n = len(rating)

        for i in range(n):
            ls = ll = rs = rl = 0

            for j in range(i):
                if rating[j] < rating[i]:
                    ls += 1
                elif rating[j] > rating[i]:
                    ll += 1
            
            for k in range(i+1, n):
                if rating[k] < rating[i]:
                    rs += 1
                elif rating[k] > rating[i]:
                    rl += 1
            count += ls*rl + ll*rs
        return count