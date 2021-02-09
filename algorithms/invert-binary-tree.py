# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

# Recursion
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.right,root.left= root.left,root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
 #iterative
    def invertTree2(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:   
                node.right,node.left= node.left,node.right
                stack += node.right,node.left
        return root
        
