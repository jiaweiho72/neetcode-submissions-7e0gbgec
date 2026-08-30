class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        30 Aug 2026
        - sliding window of size k, log the max in the window at every slide
        
        brainstorm
        - need to be able to keep track of max optimally
        - tracking max in a variable not enough, second max and so on also needed
        bruteforce
        - for each window, loop through all k to find max
        how to know which is next smallest

        Optimal
        - max usually can maintain a heap but you can't pop random element
            - (DEPRECATED)maybe you can leave it in. but keep track of left elements you removed in a dict
                - if top of heap value is in the dict, pop the value and decrement the dict until no more
                    then you can get the max
            - max_heap can contain the index of the original value.
                - if heap top is outside of range, pop it out of heap and look for max in the next heap top
                - 
        Time: 
        - maintaining a heap of size n
        - (n-k) main iterations
            - pop from heap logn
        - but total time from popping is + nlogn (worst case you need to pop all elements)

        note: max_heap use negative numbers
        pitfall: 
        - forgot to include the max of the first window
        - forgot that you need to heappush in the initing of window to actually build it. 
            - else it is an invalid heap
        """
        import heapq

        n = len(nums)
        max_heap = [] # negative
        result = []

        # 1) Init window
        for i in range(k):
            num = nums[i]
            heapq.heappush(max_heap, (-num, i))
        result.append(-max_heap[0][0])

        # 2) main sliding window
        for r in range(k, n):
            num = nums[r]
            heapq.heappush(max_heap, (-num, r))

            # check the max top
            top_val, top_index = max_heap[0]
            l = r - k + 1 # inclusive or cur element at r
            while top_index < l: # out of range
                heapq.heappop(max_heap)
                top_val, top_index = max_heap[0]
            
            result.append(-top_val)
            
        return result










