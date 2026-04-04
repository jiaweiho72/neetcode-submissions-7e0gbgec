class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        30 Mar 26
        - Two pointer (decrement or increment left/right pointer)
        - maintain a hashmap and check if complement exists in map
        - need the index so hashmap
        """

        n = len(nums)
        hashmap = {}

        for i in range(n):
            cur = nums[i]
            complement = target - cur
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[cur] = i
        return [0,0]

