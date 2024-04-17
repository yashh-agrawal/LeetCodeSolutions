# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        st = {}
        ts = {}
        for i in range(n):
            cs = s[i]
            ct = t[i]
            if cs not in st and ct not in ts:
                st[cs] = ct
                ts[ct] = cs
            elif cs in st and st[cs] != ct:
                return False
            elif ct in ts and ts[ct] != cs:
                return False
        return True