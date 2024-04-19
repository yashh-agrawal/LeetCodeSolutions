# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        arr = []
        for i in strs:
            sorted_string = ''.join(sorted(i))
            if sorted_string not in table:
                table[sorted_string] = [i]
            else:
                table[sorted_string].append(i)
        return table.values()

        