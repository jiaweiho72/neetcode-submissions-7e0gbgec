class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        23 July 2026
        - all possible subsets (varying sizes) -> backtracking
        - must not contain duplicate subsets

        backtracking(i)
        - external list
        - add or don't add current item (as it is not fixed size and list can be any size)
            - add + dfs
            - remove + dfs
        - to prevent duplicates
        - given elements are unique -> no chance of duplicates

        Time: O(2^n * n)
        - n for the list copy at the leaf node
        - 2 choices
            - n depth
                - 2^n leaf nodes
        Space: O(n*2^n)
        - insignificant
            - cur_set O(n)
            - recusion stack O(n)
        - 2^n subsets
            - *n as each subset is on average n/2


        """

        cur_set = []
        n = len(nums)
        result = []
        def backtracking(i):
            if i >= n: # out of bounds
                result.append(cur_set.copy())
                return
            
            cur = nums[i]
            # use
            cur_set.append(cur)
            backtracking(i + 1)

            # don't use
            cur_set.remove(cur)
            backtracking(i + 1)
        backtracking(0)
        return result




        
        """
        7 apr 2026 after apple
        - return all possible subsets
        - solution must not contain duplicates
        - result includes empty set

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





