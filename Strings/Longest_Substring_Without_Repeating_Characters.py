# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = 0
        cs = set()

        for right in range(len(s)):
            while s[right] in cs:
                cs.remove(s[left])
                left += 1
            cs.add(s[right])
            count = max(count, right-left+1)
        return count 