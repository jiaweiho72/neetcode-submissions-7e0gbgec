# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        5 Apr 2026
        - reversed order
        - no leading zero

        return sum as a Linked List

        solution
        - iterate through the list
            - >10 carry over to the next sum
        - edge cases
            - last 10 must be added
            - different lengths
        """

        dummy = ListNode()
        result = dummy
        carryover = 0
        while l1 or l2: # stop if anyone is empty
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            cur_sum = l1_val + l2_val
            if carryover > 0:
                cur_sum += carryover
                carryover = 0
            if cur_sum >= 10:
                carryover = 1
                cur_sum %= 10
            result.next = ListNode(cur_sum)
            result = result.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next


        if carryover > 0:
            result.next = ListNode(carryover)

        return dummy.next
            
            










