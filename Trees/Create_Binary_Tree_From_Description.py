# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent
# of childi in a binary tree of unique values. Furthermore,

# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.

# The test cases will be generated such that the binary tree is valid.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = {}
        hasParent = set()

        for parent, child, isleft in descriptions:
            if parent not in mp:
                mp[parent] = TreeNode(parent)
            if child not in mp:
                mp[child] = TreeNode(child)
            hasParent.add(child)
        
        root = None
        for parent, child, isleft in descriptions:
            if isleft == 1:
                mp[parent].left = mp[child]
            else:
                mp[parent].right = mp[child]
            if parent not in hasParent:
                root = mp[parent]
        return root