# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# Given a linked list, swap every two adjacent nodes and return its head.
# Uses only constant extra space
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        newHead = head.next
        curr = newHead
        prev = head
        while curr:
            prev.next = curr.next #Swap two adjacent nodes
            curr.next = prev
            prevPrev = prev

            prev = prev.next #Advance to the next two
            curr = prev.next if prev else None
            prevPrev.next = curr if curr else prev #Modify pointer of second node in previous pair to second node in current

        return newHead
