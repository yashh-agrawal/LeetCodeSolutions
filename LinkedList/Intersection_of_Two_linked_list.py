# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        first = headA
        second= headB

        while first != second:
            first = headB if first is None else first.next
            second = headA if second is None else second.next
        return first

# Approach 2

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        s = set()
        while headA:
            s.add(headA)
            headA = headA.next
        while headB:
            if headB in s:
                return headB
            headB = headB.next
        return None