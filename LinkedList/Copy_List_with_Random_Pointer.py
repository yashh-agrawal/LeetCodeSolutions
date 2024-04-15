# A linked list of length n is given such that each node contains an additional random pointer,
# which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
# where each new node has its value set to the value of its corresponding original node. 
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers 
# in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes 
# in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        cur = head
        while cur:
            newNode = Node(cur.val, cur.next)
            cur.next = newNode
            cur = newNode.next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        old_head = head
        new_head = head.next
        cur_old = old_head
        cur_new = new_head

        while cur_old:
            cur_old.next = cur_old.next.next
            cur_new.next = cur_new.next.next if cur_new.next else None
            cur_old = cur_old.next
            cur_new = cur_new.next
        
        return new_head

        