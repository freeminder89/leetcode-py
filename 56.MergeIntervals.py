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
        result = []
        for i in intervals:
            if not result:
                result.append(i)
            else:
                added = False
                for j in range(len(result)):
                    if i.end < result[j].start:
                        result.insert(j, i)
                        added = True
                    elif i.start > result[j].end:
                        continue
                    else:
                        result[j].start = min(i.start, result[j].start)
                        result[j].end = max(i.end, result[j].end)
                        added = True
                if not added:
                    result.append(i)
        return result




test = []
for i in [[1,3],[2,6],[8,10],[15,18]]:
    test.append(Interval(i[0], i[1]))
print [(i.start, i.end) for i in Solution().merge(test)]