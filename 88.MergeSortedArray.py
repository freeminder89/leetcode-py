__author__ = 'amow'
class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.

    def merge(self, nums1, m, nums2, n):
        i = j = 0
        while j < n:
            if i >= m or nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop(-1)
                j += 1
                m += 1
            i += 1