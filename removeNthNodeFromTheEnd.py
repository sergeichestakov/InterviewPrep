# Given a linked list, remove the n-th node from the end of list and return its head.
# Assume n will be valid
# Done in one pass!
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None: #List of length 1
            return []
        length = 1
        nthNode = head
        curr = head
        prev = None
        while curr.next:
            #If length exceeds n, move the nth node up and keep track of previous one
            if length >= n:
                prev = nthNode
                nthNode = nthNode.next
            #Traverse the list until the end
            curr = curr.next
            length += 1

        if prev is None: #List of length 2
            return nthNode.next

        prev.next = nthNode.next #Remove
        return head
