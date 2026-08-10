class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        # Initialize the heap with the first `k` elements from `nums` or adjust if `nums` has more than `k`
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            # Only push to heap if the new value is larger than the smallest value in the heap
            if val > self.min_heap[0]:
                heapq.heapreplace(self.min_heap, val)
        
        # The root of the heap is the k-th largest element
        return self.min_heap[0]
        
