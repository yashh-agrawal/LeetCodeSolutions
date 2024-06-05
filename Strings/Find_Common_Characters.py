# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
# You may return the answer in any order.


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_count = Counter(words[0])
        
        for word in words[1:]:
            word_count = Counter(word)

            for char in common_count:
                common_count[char] = min(common_count[char], word_count[char])
        
        res= []
        for char, count in common_count.items():
            res.extend([char] * count)
        
        return res