# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
# The path must contain at least one node and does not need to go through the root.
class Solution:
    MaxPath = -float('inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.subTreeSum(root)
        return self.MaxPath

    #Calculates the sum of a subtree starting at a given node
    def subTreeSum(self, node):
        if node is None:
            return 0
        left = max(0, self.subTreeSum(node.left))
        right = max(0, self.subTreeSum(node.right))
        sum = node.val + left + right
        self.MaxPath = max(self.MaxPath, sum)
        return node.val + max(left, right)
