# We can shift a string by shifting each of its letters to its successive letter.

# For example, "abc" can be shifted to be "bcd".
# We can keep shifting the string to form a sequence.

# For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
# Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for i in strings:
            differences = tuple((ord(i[s+1]) - ord(i[s])) % 26 for s in range(len(i)-1))
            table[differences].append(i)
        return table.values()