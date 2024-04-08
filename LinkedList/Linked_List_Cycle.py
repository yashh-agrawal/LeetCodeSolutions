# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the 
# next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Tortoise and Hare approach

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = fast = head

        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False

# Use Set to remember visited values
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit = set()
        cur = head

        while cur:
            if cur in visit:
                return True
            visit.add(cur)
            cur = cur.next
        return False