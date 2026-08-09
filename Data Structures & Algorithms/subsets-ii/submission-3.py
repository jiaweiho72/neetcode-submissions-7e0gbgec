class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        9 Aug 2026
        - given DUPLICATE nums, return all possible subsets
        """
        n = len(nums)
        nums.sort()
        result = []

        def dfs(i, path):
            # base case
            result.append(path.copy())

            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]: # duplicate
                    continue
                path.append(nums[j])
                dfs(j + 1, path)
                path.pop()

        dfs(0, [])
        return result




        



        """
        3 Aug 2026
        - nums may contain duplicates
        - return all possible subsets (set -> no order no size)
            - ensure no duplicates
        - not permutations so no order

        idea
        - sort
        dfs(i) -> returns 
        go through every item in nums and choose/don't choose
        - don't look backwards
        - skip while next nums is same
        - duplicate happens when you don't choose now but choose the next index and it is still the same
            - it is not duplicate if you choose this index and then process another same element
        """

        n = len(nums)
        result = []
        cur_subset = []
        nums.sort()

        def dfs(i):
            if i >= n:
                result.append(cur_subset.copy()) # O(n)
                return
            
            cur_num = nums[i]
            # 1) choose
            cur_subset.append(cur_num)
            dfs(i + 1)

            # 2) Don't choose
            cur_subset.pop()
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return result