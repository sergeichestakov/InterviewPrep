# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# Meaning the left subtree must only contain nodes with values less than the root nodes value
# And the right subtree must only contain nodes with values greater than the root nodes value

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        values = []
        self.inOrder(values, root)

        #Perform in order traversal and check that the values are sorted
        for index in range(1, len(values)):
            if values[index - 1] >= values[index]:
                return False

        return True

    def inOrder(self, values, node):
        if node:
            self.inOrder(values, node.left)
            values.append(node.val)
            self.inOrder(values, node.right)
