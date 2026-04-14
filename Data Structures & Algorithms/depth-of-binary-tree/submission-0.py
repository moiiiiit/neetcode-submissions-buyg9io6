# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_depth=0
        self.explore_node(root)
        return self.max_depth
    
    def explore_node(self, node, depth=1):
        if not node:
            self.max_depth = max(self.max_depth, depth-1)
            return
        self.explore_node(node.left, depth+1)
        self.explore_node(node.right, depth+1)