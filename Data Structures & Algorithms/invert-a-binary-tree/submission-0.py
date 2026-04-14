# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert_node_children(root)
        return root
    
    def invert_node_children(self, node):
        if not node:
            return
        left_node = node.left
        node.left = node.right
        node.right = left_node
        self.invert_node_children(node.left)
        self.invert_node_children(node.right)