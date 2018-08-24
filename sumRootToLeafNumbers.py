# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

	# Find all root to leaf paths
        nums = []
        self.sumChildren(root, [], nums)

	sum = 0
        # Recreate number from each array returned and sum
        for res in nums:
            power = len(res) - 1
            num = 0
            for digit in res:
                num += digit * pow(10, power)
                power -= 1

            sum += num

        return sum

    # Recursive function to find all root to leaf numbers
    def sumChildren(self, node, arr, nums):
        # Add value
        arr.append(node.val)
        if not node.right and not node.left: # Reached a leaf so save value
            nums.append(arr)

        # Check children if they exist
        if node.left:
            self.sumChildren(node.left, arr[:], nums)
        if node.right:
            self.sumChildren(node.right, arr[:], nums)

