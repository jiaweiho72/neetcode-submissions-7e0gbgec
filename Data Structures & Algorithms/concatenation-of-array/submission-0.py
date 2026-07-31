class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        1 Aug 2026
        - basically return ans list where it's a concatenation of two copies side by side

        idea
        - pass through nums twice. no two ways about it
        """

        ans = []
        n = len(nums)
        for i in range(2 * n):
            num_index = i % n
            ans.append(nums[num_index])
        return ans