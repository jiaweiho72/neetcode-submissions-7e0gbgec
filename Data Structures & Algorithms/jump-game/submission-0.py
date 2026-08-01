class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        2 Aug 2026
        - DP works but greedy is most optimal
        DP is O(n^2)
        - n iterations inside you also visit every other possible n values
        
        idea - greedy
        - iterate from the back
        - keep a goal index
            - it is the closest index you have to at least reach to have a path to the end
            - it is because of the property where nums[i] is the max number of jumps you can take
                - so you can jump anywhere from 0 to x distance
            - there won't be a case where you will be missing an answer
                - [1, 100, 0, 0, 1, 1]
                - I fear I may miss a path where jumping to a place with a very large jump
        """

        n = len(nums)
        goal = n - 1 # leftmost index that must at least reach to get to the end

        for i in range(n - 1, -1, -1):
            cur_possible_jumps = nums[i]
            if i + cur_possible_jumps >= goal: # It can exceed the target
                goal = i
        
        return goal == 0







