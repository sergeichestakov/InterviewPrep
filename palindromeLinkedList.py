# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# Given a singly linked list, determine if it is a palindrome.

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []

        # Populate a stack so values are stored in reverse order
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next

        # Compare list values to stack values
        numNodes = len(stack)
        for _ in range(numNodes // 2):
            val = stack.pop()
            if val != head.val:
                return False
            head = head.next

        return True
