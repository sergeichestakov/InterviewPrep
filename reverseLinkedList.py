# Reverse a singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        prev = None
        curr = head
        while curr.next:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        curr.next = prev

        return curr
