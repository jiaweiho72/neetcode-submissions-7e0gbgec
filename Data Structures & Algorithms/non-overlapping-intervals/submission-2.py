class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        21 Nov 2026

        - return min no of intervals to remove to ensure non-overlapping
        - greedy
            - if two overlap now, remove the one with the longer end as that would overlap more
            which means must remove more
        - in this case, same position is not overlapping

        [1,2],[1,4],[2,4]
        """

        n = len(intervals)
        intervals.sort()
        overlap_start, overlap_end = intervals[0]
        remove_count = 0
        for cur_start, cur_end in intervals[1:]:
            if overlap_end <= cur_start: # equals as touch is not overlap in this case
                # place overlap and reset overlap with cur
                overlap_start, overlap_end = cur_start, cur_end

            else: # means overlap -> suck up and combine
                # you want to remove as little -> keep the smaller window and remove the larger
                overlap_end = min(overlap_end, cur_end)
                remove_count += 1 # remove one and merge together

        return remove_count











        """
        23 July 2026
        - return min no of intervals to REMOVE to make rest non-overlaping
        note: Note that intervals which only touch at a point are non-overlapping

        brainstorm
        - there may be one big interval overlapping a lot
        suppose ... | \ |          \
            - greedily it is better to remove the || as it's end is shorter and overlaps less
                - does not matter the start point as previous iteration would have already considered and joined
            - iterate one by one and compare previous

        Idea
        - sort the intervals first
            - don't need to care about the start
        - greedy: 
        note: since sorted intervals and not inserting a brand new, there won't be a case where insert_interval is on the right of cur_interval
        """

        n = len(intervals)
        intervals.sort()
        remove_count = 0
        prev_start, prev_end = intervals[0][0], intervals[0][1]


        for i in range(1, n):
            cur_start, cur_end = intervals[i]

            # Check if overlapping first
            if prev_end <= cur_start: # equals not overlapping
                prev_start, prev_end = cur_start, cur_end
            else:
                # Greedily remove the larger ending
                prev_end = min(prev_end, cur_end)
                
                # simulate remove
                remove_count += 1

        return remove_count