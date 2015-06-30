__author__ = 'amow'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        node = head
        pre = None
        while node:
            if node.val == val:
                if pre:
                    pre.next = node.next
                else:
                    head = node.next
            else:
                pre = node
            node = node.next
        return head
