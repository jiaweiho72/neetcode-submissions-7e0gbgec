"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        min no of days = max no of overlapping intervals (conflict) at any point of time
        - because every conflict means need a new day

        note: meetings at same time don't overlap

        reason for sorting: so you can just compare the end

        [(2,4), (3,6), (5,8), (7,9), (7,9), (7,9)] -> 4
        2---4
          3---6
            5---8
               7--9
               7--9
               7--9
        Logic:
        - when (7,9) comes, it must check start against 8 and not 6
        - the thing is that there must be an extra idea to pop 6 away
        so that 8 is the minimum
            - 
        """
        import heapq

        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: (x.start, x.end))
        n = len(intervals)
        min_heap = [intervals[0].end]

        for i in range(1, n):
            cur_start = intervals[i].start
            cur_end = intervals[i].end
            if cur_start >= min_heap[0]: # If can be same room
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, cur_end)
            
        return len(min_heap)







