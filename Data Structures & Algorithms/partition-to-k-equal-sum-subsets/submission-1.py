class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        13 Oct 2026
        - return true if can divide array into k subsets where sum equal
            - similar to form a square where k = 4
        
        idea
        - conditions:
            - must use all elements
            - nums has duplicates (counts of 1 to 4)
                - does not matter here as it is a single path down kind of with the index i
                - duplicates is cross level and not same level
        - dfs(i)
            for k
                - try inside
            return boolean
        """

        n = len(nums)
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False # not a multiple of k -> unable to divide by k sides
        side_length = total_sum // k
        sides = [0] * k
        
        # Optimisation 1)
        nums.sort(reverse=True) # fail early with big and end early
        
        def dfs(i):
            if i == n and len(set(sides)) == 1:
                return True
            cur = nums[i]
            side_visited = set()
            for j in range(k):
                # Optimisation 2) if two sides are equal, no diff if you add in either sides
                if sides[j] in side_visited:
                    continue
                side_visited.add(sides[j])

                if sides[j] + cur > side_length: # OOB - invalid -> skip
                    continue
                sides[j] += cur
                if dfs(i + 1):
                    return True
                sides[j] -= cur
            
            return False # if no early return True

        return dfs(0)










