# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Attempt 2
        1) Fast-slow pointer to get to mid and end point
        2) Reverse the right side (mid to end)
        3) Merge two linked lists
        """

        slow, fast = head, head

        # 1) Fast slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2) Reverse second half of list
        """
        Important: note that the first half is still dangling pointing to the mid point
        they are not separate and it is like an L shape
        """
        cur = slow # slow is the midpoint
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp
        
        # 3) Merge
        first, second = head, prev
        while second.next:
            tmp1 = first.next
            first.next = second
            tmp2 = second.next
            second.next = tmp1

            first = tmp1
            second = tmp2

        return