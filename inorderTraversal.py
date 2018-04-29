# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Return the inorder traversal of a given binary tree
class Solution:
    def visit(self, node, arr):
        if (node):
            self.visit(node.left, arr)
            arr.append(node.val)
            self.visit(node.right, arr)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        self.visit(root, arr)
        return arr
