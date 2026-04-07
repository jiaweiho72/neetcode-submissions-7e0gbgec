class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        7 apr 2026 after apple
        - return all possible subsets
        - solution must not contain duplicates
        - include empty set

        if nums is not unique -> possibility of duplicates
        - like 1, 1
        
        why backtracking, needs to return every combination so can't skip some like in DP
        """

        cur = []
        result = []
        n = len(nums)
        def backtracking(i):
            if i >= n:
                # out of bounds = end = add to result
                result.append(cur.copy())
                return 
            
            # include current num
            cur.append(nums[i])
            backtracking(i + 1)

            # exclude current num
            cur.pop()
            backtracking(i + 1)
            return

        backtracking(0)
        return result





