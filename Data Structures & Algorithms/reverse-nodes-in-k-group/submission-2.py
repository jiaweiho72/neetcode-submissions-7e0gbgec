# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        6 Sep 2026
        - reverse in batches of k
        - only can modify the next pointer, not the value


        idea
        - reversing you need to keep track of the before_left and after right node
            - so that after reversing, you know where to attach back
                - because when you reverse, the right element now becomes on the left, so you can't just 
                    continue to the after_right node
                - how reversing works is that it only reverse the direction of the pointer.
                    but it does not flip the linked list like you expect
        - edge case is the starting k of ending, where before_left and after_right is None

        dummy
        - before_left is now the dummy, after_right is k + 1
        - keep track of start and end too
        - reverse 1 to k
        - attach back: before_left -> end; start -> after_right

        - if list is multiples of k, it should be ok: start -> None
        - if list has remainder, also ok: just set after_right as that after it TRIES
        to iterate k but no more

        note: can't use forloop like other question, as you don't know when really is the end of LL
        forgot: if count less than k, don't reverse. Need to check first
        mistake: doing check loop at every batch UNTIL THE END node is costly. Just count once at the start

        Time: O(n + n)
        Space: O(1) inplace, no result list
        37.40
        """

        dummy = ListNode(val=None, next=head) # dummy -> head

        before_left = dummy
        cur = head

        # 1) get remainder
        temp = cur
        nodes_count = 0
        while temp:
            nodes_count += 1
            temp = temp.next
        no_of_batches = nodes_count // k

        for _ in range(no_of_batches): # for each k
            # iterate k and reverse
            count = 0
            prev = before_left
            start = cur


            while cur and count < k: # if count is k, means already done k times -> skip
                temp_next = cur.next
                cur.next = prev

                prev = cur
                cur = temp_next
                count += 1
            end = prev
            after_right = cur
            # cur now is after k, prev is k
            before_left.next = end
            start.next = after_right

            before_left = start

        return dummy.next








