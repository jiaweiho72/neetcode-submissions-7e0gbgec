class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        22 Jul 2026
        - merge all overlapping intervals
        - return array of non-overlapping intervals 

        cases
        - insert is left of cur 
            -> input insert
            - cur become the new insert (may merge with future)
        - insert and cur overlap, merge together min and max
        - insert is right of cur -> insert cur


        note: not sorted

        """
        intervals.sort()
        n = len(intervals)
        insert_start, insert_end = intervals[0][0], intervals[0][1]
        result = []

        for i in range(1, n):
            cur_start, cur_end = intervals[i]

            if insert_end < cur_start: # insert on the left side
                result.append([insert_start, insert_end])

                insert_start, insert_end = cur_start, cur_end # set cur as the next to insert
            elif cur_end < insert_start: # insert is on the right side ( this case technically won't happen as sorted)
                result.append([cur_start, cur_end])
            else: # they overlap
                insert_start = min(insert_start, cur_start)
                insert_end = max(insert_end, cur_end)
        
        result.append([insert_start, insert_end])

        return result

