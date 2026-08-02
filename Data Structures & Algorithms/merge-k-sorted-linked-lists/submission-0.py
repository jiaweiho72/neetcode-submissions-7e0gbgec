# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Try 2
        - Instead of creating a new heap everytime where there is a lot of dup
            - create once and maintain it
        - keep iterating while there is still a min_heap to pop
        - each iteration you interact with ONE linked list
            - only pop the min and then push the next element from the same linked list

        * order by the val then index then node. 
            - As there may be ties in val so it never has to compare node objects in ties
            - you'll get this error: TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'

        min_heap is good as every step you just need the max, no need everything sorted
        iterate by min_heap rather than col by col -> when a LL reach end, it's just not pushed to heap
        """
        import heapq

        # Initialise
        min_heap = [] # (val, idx, node)
        for i in range(len(lists)):
            node = lists[i]
            if node:
                min_heap.append((node.val, i, node))
        heapq.heapify(min_heap)

        dummy = ListNode()
        tail = dummy
        
        # Main loop
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)   
            tail.next = node
            tail = tail.next
            node = node.next
            if node:
                heapq.heappush(min_heap, (node.val, idx, node))
        
        return dummy.next