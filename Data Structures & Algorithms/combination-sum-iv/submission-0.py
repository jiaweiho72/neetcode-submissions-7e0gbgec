class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        return no of combinations that sum to target
        - dfs(i) -> return no of combinations that sum to target
            - this would require keeping track of cur_sum 

        not like coin change where dfs(a) -> min no of coins
        - not unlimited no of coins

        dfs(target) -> no of ways?

        mistake: 
        - can reuse
        - permutation counts too


        """
        from functools import cache
        n = len(nums)

        @cache
        def dfs(cur_sum):
            no_of_combinations = 0

            if cur_sum == target:
                no_of_combinations += 1

            for j in range(n): # use j
                if cur_sum + nums[j] > target:
                    continue
                no_of_combinations += dfs(cur_sum + nums[j])
            return no_of_combinations
        
        return dfs(0)
                

