class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
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
        # def backtracking(cur_list, cur_sum, i):
        #     if cur_sum == target:
        #         result.append(cur_list.copy())
        #         return
        #     if i > n: # out of bounds
        #         return
        #     if cur_sum > target:
        #         return
        #     for j in range(i, n):
        #         num = nums[j]
        #         cur_list.append(num)
        #         backtracking(cur_list, cur_sum + num, j)
        #         cur_list.pop()

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
            


