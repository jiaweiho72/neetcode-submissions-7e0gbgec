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
        23 July 2026
        - return min no of rooms to schedule all meetings without overlap
            - every overlap needs one additional room
            - count max no of concurrent overlap
        
        two pointer method
        - sorted start time, sorted end time
        - go through in order and process first the earlier time (if tie, process the end first)
        - have a counter to track the current point in time overlap


        edge cases
        - all start finished and only left with end. No need to continue, already found the max
            - subsequent iterations will only release the rooms
        - all end finished and left with only start. Not possible as at least one end after the last start
        """

        n = len(intervals)
        start_times = []
        end_times = []
        for interval in intervals:
            start_times.append(interval.start)
            end_times.append(interval.end)
        start_times.sort()
        end_times.sort()

        start, end = 0, 0
        max_count = 0
        cur_count = 0
        while start < n and end < n:
            if end_times[end] <= start_times[start]: # process end first in this case
                cur_count -= 1 # a meeting has ended and can release the room
                end += 1
            else: # process start time
                cur_count += 1 # new meeting at this time
                max_count = max(max_count, cur_count)
                start += 1
        
        return max_count















        """
        
        - mainly need to keep track of the prev_end, prev_start not important as sorted

        mistake:
        - example 1
            - need to count overlap at the same time period

        - you need to constantly know the min end time
        minheap
        - minheap stores end times and each one is a 'room'
        - if minheap earliest end time before the cur_start
            - you basically reuse that room and update the next timing
        - else, means that there is overlap and you create a new room and put in this end time

        final len of heap is the max rooms used at once
        - the reason why you don't need to check inbetween is because rooms are reused by new meetings
        - one thing that don't make sense is that you have all these meeting rooms at the end,
            but it doesn't mean that is the current number of rooms at the point of end, the heap
            may still store if not popped. 
        Basically only new rooms added when there overlap and if no overlap, update the room end time
        """

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







