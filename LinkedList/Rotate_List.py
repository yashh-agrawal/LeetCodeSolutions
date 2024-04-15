# Given the head of a linked list, rotate the list to the right by k places.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0 :
            return head
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next
        k = k % length
        if k == 0:
            return head
        newCur = head
        for i in range(length - k - 1):
            newCur = newCur.next
        newHead = newCur.next
        newCur.next = None
        cur.next = head
        return newHead