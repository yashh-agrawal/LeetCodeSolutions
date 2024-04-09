# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, 
# and return the new head.

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        current = head
        while current:
            if current.val==val:
                first.next = current.next
            else:
                first = current
            current = current.next
        return dummy.next 