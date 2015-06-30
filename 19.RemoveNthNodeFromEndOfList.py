__author__ = 'amow'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        tmpn = ListNode(-1)
        tmpn.next = head
        t1 = t2 = tmpn
        for i in xrange(n):
            t2 = t2.next
        while t2 and t2.next:
            t2 = t2.next
            t1 = t1.next
        t1.next = t1.next.next
        return tmpn.next