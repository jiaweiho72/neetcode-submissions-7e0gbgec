class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Idea: Max/min heap
        let n be the size of nums
        1) I will first build a max heap - O(n)
        2) I will pop K times - O(k * logn)
        - return the kth poped element
        """
        import heapq

        # Reverse to convert to max_heap
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap) 

        # Pop K times
        result = 0
        for i in range(k):
            result = heapq.heappop(max_heap)
        return - result # Convert back to positive
