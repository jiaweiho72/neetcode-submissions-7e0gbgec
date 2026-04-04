"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        If can add all meetings -> all intervals don't overlap

        Idea:
        - Iterate for each interval
            - If current start is less than the prev end (maximum):
                - invalid
            - Update prev end
        note: exclusive -> (0,8),(8,10) is not considered a conflict at 8

        - Sort by start time so that you just need to check the cur start
        if before the end -> auto assumption that cur start is always >= 
        than the prev starts
            - so that you can iterate one time in order
        """

        intervals.sort(key=lambda i: (i.start, i.end)) # Sort by first then second ele
        n = len(intervals)
        max_end = float('-inf')
        for i in range(n):
            cur_start = intervals[i].start
            cur_end = intervals[i].end

            if cur_start < max_end:
                return False
            max_end = max(max_end, cur_end)

        return True



