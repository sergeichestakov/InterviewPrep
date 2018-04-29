# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def visit(self, node, arr):
        if node:
            arr.append(node.val)
            self.visit(node.left, arr)
            self.visit(node.right, arr)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
	self.visit(root, arr)
        return arr
