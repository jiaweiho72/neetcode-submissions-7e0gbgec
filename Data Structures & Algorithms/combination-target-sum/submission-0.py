class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        input: distinct nums, int target
        output: list of all 'unique' comb where sum = target

        backtracking - there is no sub problem
        - for uniqueness -> 
        """
        result = []
        n = len(nums)
        def backtracking(cur_list, cur_sum, i):
            if cur_sum == target:
                result.append(cur_list.copy())
                return
            if i > n: # out of bounds
                return
            if cur_sum > target:
                return
            for j in range(i, n):
                num = nums[j]
                cur_list.append(num)
                backtracking(cur_list, cur_sum + num, j)
                cur_list.pop()
        backtracking([], 0, 0)
        return result
            


