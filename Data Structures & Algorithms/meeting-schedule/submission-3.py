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
        23 July 2026
        - determine if there are any conflicts (overlaps)
        - return boolean

        - touching is not counted as overlap

        Time: O(nlogn)
        """

        intervals.sort(key=lambda i: (i.start, i.end))
        n = len(intervals)
        if not intervals:
            return True
        prev_start, prev_end = intervals[0].start, intervals[0].end

        for i in range(1, n):
            cur_start, cur_end = intervals[i].start, intervals[i].end

            # compare if not overlap
            if prev_end <= cur_start:
                prev_start, prev_end = cur_start, cur_end

            else: # means overlap found
                return False
        return True














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



