# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.level_order_traversal=defaultdict(list)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse_level(root, 0)
        return list(self.level_order_traversal.values())
    
    def traverse_level(self, node, level):
        if not node:
            return
        # Add node to traversal
        self.level_order_traversal[level].append(node.val)
        # Traverse left
        self.traverse_level(node.left, level+1)
        # Traverse right
        self.traverse_level(node.right, level+1)