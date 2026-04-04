# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        5 apr 2026
        - return boolean if cycle found

        naive
        - hashmap but takes extra space

        Technique
        - fast slow pointer will meet if there is a cycle
        - if there is no cycle, loops ends when fast pointer hits null
        - if cycle exists, each cycle will reduce gap between fast and slow pointer as the fast is chasing the slow by one index

        """

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

            if slow == fast: # put after as initial is head head and always true
                return True
        
        return False





