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
        before_start -> start -> end -> after_end
        pitfalls
        # edge case: no elements on the left
            - need dummy node to 

        Time: O(n) where n is from start of linked list to right
        Space: O(1)
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

        index = left # start from left
        while index <= right: # stop cur exactly when it reaches right
            next_temp = cur.next
            cur.next = prev

            prev, cur = cur, next_temp
            index += 1
        end = prev
        after_end = cur
        
        # 3) Relink back reversed list
        if before_start.val: # if not none -> there is a before_left portion
            before_start.next = end
        else: # else, left is the first element -> just update the dummy pointer
            dummy.next = end
        start.next = after_end

        return dummy.next










