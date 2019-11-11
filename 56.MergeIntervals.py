class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "%s, %s" % (self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        points = []
        for i in intervals:
            added = False
            merge_end = False
            for j in range(len(points)):
                s, e = points[j]
                if merge_end is not False:
                    if merge_end < s:
                        break
                    points[j] = [merge_end, max(merge_end, e)]
                    continue
                if i.end < s:
                    points.insert(j, [i.start, i.end])
                    added = True
                    break
                elif i.start > e:
                    continue
                else:
                    points[j] = [min(i.start, s), max(i.end, e)]
                    merge_end = points[j][1]
                    added = True
            if not added:
                points.append([i.start, i.end])
        result = []
        for p in points:
            if (not result) or result[-1].end != p[0]:
                result.append(Interval(p[0], p[1]))
            else:
                result[-1].end = p[1]
        return result


test = []
for i in [[1, 2], [3, 4], [5, 11], [1, 10], [12, 15]]:
    test.append(Interval(i[0], i[1]))
print [(i.start, i.end) for i in Solution().merge(test)]
