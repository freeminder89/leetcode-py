# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        current = head
        result = head.next
        pre = None
        while current is not None and current.next is not None:
            n = current.next
            rest = n.next
            n.next = current
            current.next = rest
            if pre is not None:
                pre.next = n
            pre = current
            current = rest
        return result


class Node():
    def __init__(self, v):
        self.v = v
        self.next = None

    def __str__(self):
        return self.v


def build_from_list(li):
    head = Node(li[0])
    pre = head
    for i in range(1, len(li)):
        n = Node(li[i])
        pre.next = n
        pre = n
    return head


def print_node(head):
    s = head
    li = []
    while s is not None:
        li.append(s.v)
        s = s.next
    print li


h = build_from_list([1, 2, 3, 4])
s = Solution()
print_node(s.swapPairs(h))
