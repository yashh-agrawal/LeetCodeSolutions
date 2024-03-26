# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = defaultdict(int)
        
        for char in magazine:
            count[char] += 1
        for char in ransomNote:
            if char not in count or count[char] <= 0:
                return False
            count[char] -= 1
        return True        
