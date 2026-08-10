class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        22 Jul 2026
        - given sorted intervals
        - to insert newInterval (merge overlapping if needed)
        - return intervals ( don't need to modify in place)

        track the insert_start and insert_end
        - if insert_start in between cur start and end -> merge -> get the min of both AKA cur start
            - insert_end is the max of cur and insert end
        
        - if insert_start > both cur and start -> insert into result
        - if insert_start < cur and start
            - if insert_end < cur start:
                insert the insert
            - else -> merge and get max of the end

        scenarios
        1) insert exclusive to the left of cur \\ ||
            - nothing to do continue, iterating
        2) only the butt of insert in cur \ | \ |
            - min and max edges
        3) insert overlap entire cur    \ || \
            - min and max edges
        4) insert fully inside cur    | \ \ | 
            - min and max edges
        5) only start of insert in cur | \ | \
            - min and max edges
        6) insert entirely after cur    || \\

        easier way to think as there is many ways of overlap, check if it completely don't overlap 
        - for overlap
            - get the min and max of the corners
        - for non-overlap
            - insert is on the left, further down there no possibility of overlap
                - insert this to result as well as the others
            - insert on the right, continue iteration
                - insert cur
                - if at the end,= still not inserted, must insert


        tip: look at cases of non overlap as there is less scenarios compared to overlap
        """

        insert_start, insert_end = newInterval
        n = len(intervals)
        result = []

        for i in range(n):
            cur_start, cur_end = intervals[i]
            # check cases of not overlap
            if insert_end < cur_start: # left side -> means done
                result.append([insert_start, insert_end])
                # return result + intervals[i:]
                insert_start, insert_end = cur_start, cur_end
            elif insert_start > cur_end: # right side
                result.append([cur_start, cur_end])
            else: # overlap
                insert_start = min(insert_start, cur_start)
                insert_end = max(insert_end, cur_end)
        
        # if reached here, means did not reach the case to insert (at the last iteration it was on the right side or overlapping)
        result.append([insert_start, insert_end])
        return result

