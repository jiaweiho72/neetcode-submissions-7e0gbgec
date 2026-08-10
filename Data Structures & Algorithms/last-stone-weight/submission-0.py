class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Max heap - better in this case to pop top k rather than maintain top k list
        n = len(stones)
        max_heap = [-s for s in stones] # negative for max_heap
        heapq.heapify(max_heap) # O(n)

        while max_heap and len(max_heap) >= 2:
            first = heapq.heappop(max_heap) # Heaviest
            second = heapq.heappop(max_heap) # Second heaviest
            if first != second: # first is heavier than second
                new_weight = first - second
                heapq.heappush(max_heap, new_weight)
        if max_heap: # not empty
            return - heapq.heappop(max_heap)
        return 0