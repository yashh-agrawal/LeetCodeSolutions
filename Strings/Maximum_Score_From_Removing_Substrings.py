# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        if y > x:
            high = "ba"
            high_score = y
            low = "ab"
            low_score = x
        else:
            high = "ab"
            high_score = x
            low = "ba"
            low_score = y
        
        stack = []
        for char in s:
            if char == high[1] and stack and stack[-1] == high[0]:
                res += high_score
                stack.pop()
            else:
                stack.append(char)
        
        new_stack = []
        for char in stack:
            if char == low[1] and new_stack and new_stack[-1] == low[0]:
                res += low_score
                new_stack.pop()
            else:
                new_stack.append(char)
        
        return res