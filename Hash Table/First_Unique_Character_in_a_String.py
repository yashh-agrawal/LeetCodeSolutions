# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Approach 1:

class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = {}
        for i, char in enumerate(s):
            if char not in res:
                res[char] = [1,i]
            else:
                res[char][0] += 1
        for char, [count, index] in res.items():
            if count == 1:
                return index
        return -1   

#Approach 2

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1
            