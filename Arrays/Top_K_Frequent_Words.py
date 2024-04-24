# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. 
# Sort the words with the same frequency by their lexicographical order.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        ans = sorted(c.items(), key=lambda x: (-x[1], x[0]))
        arr = []
        for key,_ in ans[:k]:
            arr.append(key)
        return arr