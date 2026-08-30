# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        30 Aug 2026
        - reverse only the portion from left to right (1 indexed)

        normal reverse
        - prev, cur
        - cur.next = prev
        - move cur to next

        1) left may not be the start - need to find the start too

        additionally need to keep track of the right side node to know where to attach to
        - (it is the next)

        1 -> [2 -> 3] -> 4 -> 5

        pitfalls
        # edge case: no elements on the left
        """
        dummy = ListNode()
        dummy.next = head
        before_start = dummy
        # 1) Find start point (beside left)
        for _ in range(1, left): # stop right beside left
            before_start = before_start.next
        
        # 2) Main reverse
        prev = None
        cur = before_start.next
        start = cur

        index = left
        next_temp = None # when end, it will store the element on the right of 'right'
        while index <= right and cur: # stop cur exactly when it reaches right
            next_temp = cur.next
            cur.next = prev

            prev, cur = cur, next_temp
            index += 1
        end = prev
        after_end = cur
        
        # 3) Relink back reversed list
        if before_start.val:
            before_start.next = end
        else:
            dummy.next = end
        start.next = after_end

        return dummy.next










