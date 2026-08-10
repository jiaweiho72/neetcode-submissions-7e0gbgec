class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        29 Jun 2026
        - return k closest points to origin (points, not he distance)
        - maintain a heap of size K 
            - always want to peek the max to compare if should be eliminated -> max heap

        - must calculate the distance
        * max heap must use negative numbers
        """
        import math
        import heapq

        max_heap = []

        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (- distance, (x,y)))
                continue
            else:
                cur_max, max_point = max_heap[0]
                if distance < - cur_max:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (- distance, (x,y)))
                else:
                    continue
        return [x[1] for x in max_heap]
        
        
        
        
        
        
        
        # k <= points.length
        # Heapq default is minheap
        min_heap = []

        # Inititalise the minheap
        for point in points:
            x, y = point
            distance = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(min_heap, (distance, point))

        result = []
        # Pop min k
        for i in range(k):
            distance, point = heapq.heappop(min_heap)
            result.append(point)

        return result
