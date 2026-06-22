"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ni = len(intervals)
        for i in range(ni):
            for j in range(i+1, ni):
                if intervals[i].end <= intervals[j].start or intervals[i].start >= intervals[j].end:
                    pass
                else:
                    return False
        return True