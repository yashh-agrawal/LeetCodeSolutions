# There is a strange printer with the following two special properties:

# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
# Given a string s, return the minimum number of turns the printer needed to print it.

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        @cache
        def count(left, right):
            if left >= right:
                return 0

            best = count(left + 1, right) + 1

            for i in range(left + 1, right + 1):
                if s[left] == s[i]:
                    best = min(best, count(left, i-1) + count(i, right))
            return best
        
        return count(0, n - 1) + 1