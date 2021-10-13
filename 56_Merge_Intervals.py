class Solution:
    def sortIntervals(self, intervals):
        def sortFn(a):
            return a[0]
        return sorted(intervals, key=sortFn)

    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals
        a = self.sortIntervals(intervals)
        res = []

        for interval in a:
            if len(res) == 0:
                res.append(interval)
            elif interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res
