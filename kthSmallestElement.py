# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        values = []
        self.inOrder(values, root)

        return values[k - 1]

    def inOrder(self, values, node):
        if node:
            self.inOrder(values, node.left)
            values.append(node.val)
            self.inOrder(values, node.right)
