# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Find the sum of all left leaves in a given binary tree.

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.sumLeaves(root.left, True) + self.sumLeaves(root.right, False)

    def sumLeaves(self, node, isLeft):
        if not node:
            return 0
        if not node.right and not node.left: #Leaf
            return node.val if isLeft else 0
        return self.sumLeaves(node.left, True) + self.sumLeaves(node.right, False)
