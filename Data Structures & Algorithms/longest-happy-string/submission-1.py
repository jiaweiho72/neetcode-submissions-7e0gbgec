class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        4 Oct 2026
        - happy string: 
            only contains a,b or c
            no subtring aaa, bbb, ccc (no 3 times in a row)
            at most x occurance of x

        - given 3 integers, return longest possible happy string
            - if multiple answer, return any
            - if no answer, return ""


        idea
        - greedy, the element with the max count should always be used first (only if valid)
            as it will lead to optimal answer
            eg. 1,2,2,2,2
            if you used 1,2,2,2, you can't add one more 2
            but if you used 2,2,2,1,2 it is ok. so using the max count will lead to optimal case
            - using less count prematurely may cause higher counts one to be unable to form valid 
            - for questions where you need to have characters not having x consecutive times
        - but the max count element is not static from the start, it changes as the max count continues to be used a lot
        - so dynamic heap to keep track of max count

        do I need a heap
        - if not: each time go through 3 iterations to find max
        - if heap: 2*log(3) to find


        Time: 30mins
        Time: max iteration n = a+b+c. each iteration do log(3) nlog3
        Space: heapq size 3, result size n
        """

        import heapq
        from collections import Counter
        max_heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')] # (count, letter) max count (negative). Count is the max possible can use
        heapq.heapify(max_heap)

        result = ""
        consecutive_cnt = 1

        while True:
            max_count, max_letter = heapq.heappop(max_heap)
            """
            If letter count hits 0, all is used. max_heap will choose other elements
            If other elements also no more, then the max_heap pop 0, meaning all are 0
            """
            
            """
            To handle the check to not choose element that will cause > 3 consecutive same element. 
            """
            if result and result[-1] == max_letter: # same as previous
                consecutive_cnt += 1
            else:
                consecutive_cnt = 1
            
            if consecutive_cnt >= 3: # current is invalid
                next_max_cnt, next_max_letter = heapq.heappop(max_heap)
                heapq.heappush(max_heap, (max_count, max_letter)) # put back prev unused letter
                max_count, max_letter = next_max_cnt, next_max_letter

            if max_count == 0:
                break

            heapq.heappush(max_heap, (max_count -- 1, max_letter)) # max count is negative

            result += max_letter

        return result









