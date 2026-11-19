class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        20 Nov 2026
        - merge all overlapping intervals to form non-overlapping output
        
        idea
        - stagger too intervals each time -> the current and the one to insert(aka currently merging)
        - you insert the merge only when it no longer overlaps the cur
            - and then you continue this relationship by swapping the cur and the merging interval
        - because you only know theres no overlap if the merge interval if it is AFTER the cur interval
            - but you can't insert the merge interval but can insert the cur first
                - then check if the merge interval overlaps with the rest
                - actually the cur is like the merge 
        - remember to append the last one at the back the merge
            - all cases will have a merge left at the back
            - because every loop guarantee you only append one. so you can't append cur and merge the same time

        note: overlap if in the same position
        
        """

        intervals.sort()
        merge_start, merge_end = intervals[0]
        result = []
        for cur_start, cur_end in intervals:
            if cur_end < merge_start: # merge on the right side -> just append cur -> continue searching for place to insert merge
                result.append([cur_start, cur_end])
            elif merge_end < cur_start: # merge on the left side -> append merge -> cur on right becomes new target to merge in
                result.append([merge_start, merge_end])
                merge_start, merge_end = cur_start, cur_end
            else: # they overlap
                merge_start = min(merge_start, cur_start)
                merge_end = max(merge_end, cur_end)
        result.append([merge_start, merge_end])

        return result









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

