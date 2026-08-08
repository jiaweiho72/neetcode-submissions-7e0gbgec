class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        BFS (greedy)
        - at each position, compute how far we can reach in one more jump
        - l, r current range of choice of possible jumps
        bfs idea: each level is a step and each level has a range of possible values for that level
        - in the next range, you update l, r =  r + 1, furthest
            - l you don't include those <= r again because you processed all these alr and already found greater ranges they can reach. If you visit them again, it is like taking extra one unecessary step again when previously it could reach beyond it. 
            - it is pointless to jump to a position that you already could jump to in the previous jump, even if this place is the optimal path

        """

        no_of_jumps = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1): # in the previously defined possible range -> get the furthest
                farthest = max(farthest, i + nums[i])
            l = r + 1 # start searching from a new range. behind this, you have all checked already in previous loop
            r = farthest
            no_of_jumps += 1
        return no_of_jumps 
            