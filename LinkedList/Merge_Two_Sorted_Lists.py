# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 or list2
        return dummy.next
        
#Approach 2 (Recursion)
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        def merge(dummy,node1,node2):

            if node1 is None and node2 is None:
                return
            if node1 is None and node2 is not None:
                return node2
            if node1 is not None and node2 is None:
                return node1
            if node1.val <= node2.val:
                dummy = node1
                dummy.next = merge(dummy,node1.next,node2)
            if node1.val > node2.val:
                dummy = node2
                dummy.next = merge(dummy,node1,node2.next)
            return dummy
        return merge(dummy,list1,list2)        