class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        22 Sep 2026
        - rearrange such that no two chars are the same
        - return "" if not possible

        bruteforce
        - every character try every position n!

        greedy
        - better to first fill and use up the one with max count
            - so that you can spread out were possible
            - rather than leaving to the end when you do not have non-elements to fill in between
            - no unoptimal case where you choose the max count element but it is better later
        - get the max count element every round. If same element as previous, get the next


        aaaxx
        - only possible answer is axaxa

        don't allow count = 0 in the max_heap

        """
        from collections import Counter
        import heapq

        # init max_heap count
        
        counts = Counter(s)
        max_heap = [[-count, char] for char, count in counts.items()]
        heapq.heapify(max_heap)

        result = ""

        while max_heap:
            count, char = heapq.heappop(max_heap)
            count *= -1
            if result and result[-1] == char: # if same adjacent -> choose next
                if not max_heap: # if no more other elements to fill inbetween -> invalid
                    return "" 

                count2, char2 = heapq.heappop(max_heap)
                count2 *= -1

                heapq.heappush(max_heap, [-count, char])
                if (count2 - 1) != 0: # don't push to heap if zero count
                    heapq.heappush(max_heap, [-(count2 - 1), char2])
                result += char2
            else:
                if (count - 1) != 0:
                    heapq.heappush(max_heap, [-(count - 1), char])
                result += char

        return result




        






