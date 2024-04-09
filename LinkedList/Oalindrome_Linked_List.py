# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next
        current = head
        while current and current.val == stack.pop():
            current = current.next
        return current is None