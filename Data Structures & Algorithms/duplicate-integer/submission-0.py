class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        1) O(n^2) 
        - every integer search the whole list

        2) O(n)
        - Hashset
        - One pass
            - check if existing in hashset
        """

        hash_set = set()
        n = len(nums)

        for i in range(n):
            num = nums[i]
            if num in hash_set:
                return True
            hash_set.add(num)

        return False



