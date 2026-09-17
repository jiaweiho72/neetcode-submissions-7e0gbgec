class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        17 Sep 2026
        - tasks are not sorted by the enqueue time
        - choose the shortes processing time and if tie, smallest index
        - enqueue is when it is able to be processed. processing not in order of enqueue

        idea
        - need the smallest every iteration -> minheap
            - sorted by processing_time then index. 
        - enqueue will only enqueue into the minheap
        - keep track of current time
            - processing each task where enqueue time is < current time -> pop out or use index
        note: sorting messes up the index, so append original index to each element
        mistake: the enqueue time may come after the 

        for same enqueue time, does not matter about ties as both will be queued into heap and heap handles
        

        at each time need to be able to have all the valid tasks ready for selection
        1) iterate per task and let enqueue time be current time
            - add task 
            - try to process but the end time may be way behind so only process when the current time is at or after processend time
            - at each point when you can process
                - you would have all the previous unprocessed in the heap
            - at the end you may have leftover in the heap where at this point in time,
            everything in the heap is valid in time to use, so you could just pop them in order
        2) while loop for each end time
            - each loop process one task at the last process end time
            - at this end time, enqueue all the tasks before this time as they have passed
            - now with the options, choose the optimal valid one
            problem, need to find the initial end time
        
        edge case, non overlap
        - now have no more queued task to process at cur time, but there are still tasks. You need to skip to the unqueued task

        when you can process, you need everything unused before to be in the heap
        """

        import heapq
        min_heap = [] # [processing_time, index]

        # append index to the back of each element
        for i, task in enumerate(tasks):
            task.append(i)
        
        tasks.sort()

        n = len(tasks)
        cur_time = tasks[0][0]
        task_index = 0

        result = []

        while min_heap or task_index < n: # while there is heap to pop or it is the first iteration(empty heap)
            # edge case: when got no more to process and there are still unenqueues, change cur_time to 
            if not min_heap:
                cur_time = max(cur_time, tasks[task_index][0])
            
            # 1) enqueue valid tasks
            while task_index in range(n) and tasks[task_index][0] <= cur_time: # while can enqueue tasks into candidates
                task = tasks[task_index]
                candidate_task = [task[1], task[2]]
                heapq.heappush(min_heap, candidate_task)
                task_index += 1
            
            # 2) Choose task to process
            selected_task = heapq.heappop(min_heap)
            cur_time += selected_task[0]
            result.append(selected_task[1])

        return result

        



        









