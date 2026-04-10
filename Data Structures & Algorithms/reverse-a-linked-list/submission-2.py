# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # """
        # 5 apr 2026
        # - next and prev swap
        # - return the head
        # """

        # prev = None
        # cur = head
        # while cur:
        #     nxt = cur.next
        #     cur.next = prev

        #     prev = cur
        #     cur = nxt # stop when cur is None -> so return the previous
        # return prev

        """
        11 Apr 2026
        need prev and next to operate any edge modification in linked list
        """

        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        return prev

        



