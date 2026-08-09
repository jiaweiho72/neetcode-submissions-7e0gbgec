class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        9 Aug 2026
        For loop 
        """
        result = []
        n = len(nums)

        def dfs(i, cur_nums, cur_sum): # i represents you can choose from pool from this index onwards
            if cur_sum == target: # valid
                result.append(cur_nums.copy())
                return 
            if cur_sum > target or i >= n: # invalid/OOB (note oob won't happen and forloop is ranged)
                return

            for j in range(i, n):
                # use current j element
                cur_nums.append(nums[j])
                dfs(j, cur_nums, cur_sum + nums[j]) # did not increment j as can reuse
                cur_nums.pop()

        dfs(0, [], 0)
        return result







        """
        Speed Run
        - combination not permutation
            - frequency of characters not the order
        - return all -> backtracking

        - Can reuse same number
        - keep track of the sum
        - search everything and break path when exceed sum
        - Main problem: need to avoid duplicates
            - split: one side i can be a candidate; other side i cannot be
            - yeah you won't start at every item anymore but only start from the first and search from there

        or you could still do the for loop method

        eg.
        - when you use 2, you can still use 2 later on
        - but then there is a problem of duplicate for this case
            - 2,3 vs 3,2
        """

        n = len(candidates)
        res = []

        def backtracking(cur, i, total):
            if total > target or i == n:
                return
            elif total == target:
                res.append(cur.copy())
                return
            
            cur.append(candidates[i])
            backtracking(cur, i, total + candidates[i])

            cur.pop()
            backtracking(cur, i + 1, total)
        
        backtracking([], 0, 0)
        return res

        """
        input: distinct nums, int target
        output: list of all 'unique' comb where sum = target

        backtracking - there is no sub problem
        - for uniqueness -> naturally if you go in order, you won't be having dups
        
        fixed traversal order-based backtracking -> unique
        - only go forward or stay


        ****
        I have to do an extra clean of str for both as I added something
        to both of the cases

        unlike normal backtracking where it's i choose to add something
        or choose to skip this. If I skip, then there is no need to modify
        the variable and since I did not modify, there is no need to 
        clean the variable. 

        - cleaning the variable is for when you return it upstream
        - say you have a parent P with value p
            - you started on the left node and added l, if you did not remove
            it would be returned pl
            - then you recursive to the right node with the current value as pl
            but the correct expectation is that the current value is p only
        """
        result = []
        n = len(nums)

        def backtracking(cur_list, cur_sum, i):
            if cur_sum == target:
                result.append(cur_list.copy())
                return
            if cur_sum > target:
                return
            if i >= n:
                return
            
            num = nums[i]

            # Select
            cur_list.append(num)
            backtracking(cur_list, cur_sum + num, i) # i as can have duplicates

            # Skip and next one will be selected in the same place
            cur_list.pop()
            backtracking(cur_list, cur_sum, i + 1)

            
        backtracking([], 0, 0)
        return result
            


