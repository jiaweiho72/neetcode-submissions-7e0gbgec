class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        HARD question - only can memorise
        
        IDEA:
        Similar to a linkedlist, find the start of the cycle.
        1) Use index as edge -> since list is size 'n + 1' and the num range is from [1, n]
        2) Use Floyd's Tortoise and Hare to find cycle:
            - First find the intersection between fast and slow pointer x
            - Let start of cycle be *
            By theory, the distance from start to * is equal to x to *
                - so they will meet at the duplicate number

        note: index 0 is not part of cycle as nums is [1, n]
        note: problem GUARANTEES there is a repeated number
            - so there will be a pigeon hole loop where there will be a cycle
            - else it will run infinitely -> unlike linkedlist where it stops when it reaches
            the end of the list which is None
        """

        slow, fast = 0, 0
        # 1) Find slow and fast pointer intersection
        while True:
            slow = nums[slow] # Traverse one step
            fast = nums[nums[fast]] # Traverse two step
            if slow == fast:
                break
        
        # 2) Find the start of the linkedlist
        start, intersection = 0, slow
        while True:
            start = nums[start]
            intersection = nums[intersection]
            if start == intersection:
                break
        
        return start