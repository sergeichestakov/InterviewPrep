# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Given a binary tree, flatten it to a linked list in-place.

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                # Save the right side and move all left nodes to the right
                oldRight = root.right
                root.right = root.left
		# Remove left side and save a pointer to next node
                root.left = None
                newRoot = root.right

                # Traverse to the end and append the previous right side
                while root.right:
                    root = root.right
                root.right = oldRight

                root = newRoot
            else: # Advance
                root = root.right
