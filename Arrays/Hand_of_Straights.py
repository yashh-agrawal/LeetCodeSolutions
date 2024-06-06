# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize,
# and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
# return true if she can rearrange the cards, or false otherwise.

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        count = Counter(hand)
        sorted_keys = sorted(count.keys())

        for key in sorted_keys:
            if count[key] > 0:
                start_count = count[key]
                for i in range(key, key + groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
        return True