class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        - Slightly greedy as it is always better to fill with the highest frequency elements.
        - if you put low freq elements, 

        if the element has only one count, it does not have to worry about any gaps in the
        future -> as there will be none


        n = 1, [A, A, A, B, B, C]
        A-B-A B-A-C
        B-A-B A-C-A
        C-A-B A-B-A
        C-B-A B-A-idle A

        n = 2, [A, A, A, B, B, C]

        A-C-B A-idle-B A
        C-A-B idle-A-B idle-A
        B-A-C B-A-idle B-idle-A
        C-B-A idle-B-A idle-idle-A
        

         n = 2
        """

        """
        Idea:
        Greedy algo where at every step, your decision should be the use the char with 
        the most frequency as there will be more idle time they have to fill in between

        1) Get the frequency of each character
        2) Keep track of a max_heap in a list -> index will be the char and value is the freq
        - Keep track of the time
        - At each step:
            - Pop the max freq item from max_heap (if it's in the heap, it is available)
            - 'Complete this task' and increment the time
            - Add the freq to the queue to be processed later 
            - Also check the first element of the queue whether it has finished it's idle
            period and can be added back (they are checked as the same time as popping 
            from the max_heap)
        
        - Use a queue so that you can queue tasks to be assigned (neater)
            - queue a tuple where (-freq , next_available_time)
        """

        from collections import Counter, deque
        import heapq
        

        min_interval = float('inf')

        # There will be 25 unique characters (keys) from A-Z
        count_dict = dict(Counter(tasks))
        max_heap = [ -freq for freq in count_dict.values()]
        heapq.heapify(max_heap)

        q = deque()
        time = 0

        while max_heap or q:
            # Do the task with the max frequency
            if max_heap:
                task_freq = heapq.heappop(max_heap)
                # Check if there are still counts of the cur element to use
                if (-task_freq -1) > 0:
                    q.append((task_freq --1, time + n))
            """
            If the head of the queue is ready to be ran again - put it into the 
            max_heap for it to process the next iteration. Else leave it. It does
            not do the task yet.
            """
            if q and q[0][1] == time:
                task_freq, next_available_time = q.popleft()
                # Push back to the max_heap without using it first
                heapq.heappush(max_heap, task_freq)
            
            # Each iteration is a time, whether task is done or not
            time += 1

        return time
