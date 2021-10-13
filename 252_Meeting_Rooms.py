class Solution:
    def canAttendMeetings(self, intervals):
        sortedIntervals = sorted(intervals, key=lambda interval: interval[0])

        for i in range(1, len(sortedIntervals)):
            if sortedIntervals[i][0] < sortedIntervals[i-1][1]:
                return False
        return True
