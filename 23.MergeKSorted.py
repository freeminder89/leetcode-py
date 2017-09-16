# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sort_heap(self, heap, current_top, heap_size):
        left = current_top * 2
        right = left + 1
        min_v = heap[current_top]
        swap_with = current_top
        smaller = lambda x, y: y < heap_size and heap[y] is not None and (x is None or x.val > heap[y].val)
        for i in [left, right]:
            if smaller(min_v, i):
                min_v = heap[i]
                swap_with = i
        if swap_with == current_top:
            return
        heap[current_top], heap[swap_with] = heap[swap_with], heap[current_top]
        self.sort_heap(heap, swap_with, heap_size)

    def init_heap(self, heap, heap_size):
        if not heap_size:
            return heap
        mid = (heap_size - 1) / 2
        for i in xrange(mid, -1, -1):
            self.sort_heap(heap, i, heap_size)

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = map(lambda x: x, lists)
        heap_size = len(heap)
        self.init_heap(heap, heap_size)
        result = []
        while heap and heap[0] is not None:
            result.append(heap[0].val)
            heap[0] = heap[0].next
            self.sort_heap(heap, 0, heap_size)
        return result
