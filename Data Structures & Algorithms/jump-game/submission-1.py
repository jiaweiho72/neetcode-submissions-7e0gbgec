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

            - each time you update the leftmost goal to guarantee you a path to the end
            - if current can at least hit the goal -> guaranteed path to end -> the target is now to reach this index

        understanding
        - you worry there may be an edge case where it does not jump to the goal. But as you iterate down, the solution path MUST be able to either reach or go beyond the goal. If it is a solution it will be able to do that and exceed. 
            - like it is more optimal to jump to a point on the left of goal
            - but the thing is you later will iterate to this point on the left and it WILL have a path that exceeds the goal and the goal will be updated
        - not the goal is the leftmost index with a path to the end. The current iteration index may be a few index left of it if these indexes don't have a path that can at least reach it. 
        """

        n = len(nums)
        goal = n - 1 # leftmost index that must at least reach to get to the end

        for i in range(n - 1, -1, -1):
            cur_possible_jumps = nums[i]
            if i + cur_possible_jumps >= goal: # It can exceed the target
                goal = i
        
        return goal == 0







