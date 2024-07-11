# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        ind_stack = deque()
        res = []
        for char in s:
            if char == "(":
                ind_stack.append(len(res))
            elif char == ")":
                start_ind = ind_stack.pop()
                res[start_ind:] = res[start_ind:][::-1]
            else:
                res.append(char)
        return "".join(res)