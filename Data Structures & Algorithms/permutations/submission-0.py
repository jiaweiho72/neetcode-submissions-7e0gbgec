class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        5 Apr
        - return list of permutations

        use and don't use

        special
        - need permutations of the remaining elements
        """

        result = []
        n = len(nums)
        visited = [False] * n  # track which numbers are used

        def backtrack(cur):
            if len(cur) == n:
                result.append(cur.copy())
                return

            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                cur.append(nums[i])
                backtrack(cur)
                cur.pop()
                visited[i] = False

        backtrack([])
        return result
