# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Base case: both null
        if not p and not q:
            return True
        # Different values
        if not p or not q or p.val != q.val:
            return False

        # Check children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

