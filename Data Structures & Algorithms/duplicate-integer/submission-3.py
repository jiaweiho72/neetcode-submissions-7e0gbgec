class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        22 Sep 2026

        - keep track of elements on the go with hashset. if seen before -> return true
        """

        visited = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in visited:
                return True
            visited.add(nums[i])

        return False





        # """
        # 1) O(n^2) 
        # - every integer search the whole list

        # 2) O(n)
        # - Hashset
        # - One pass
        #     - check if existing in hashset
        # """

        # hash_set = set()
        # n = len(nums)

        # for i in range(n):
        #     num = nums[i]
        #     if num in hash_set:
        #         return True
        #     hash_set.add(num)

        # return False

        """
        Back again
        - keep track and check hashset
        """

        hashset = set()
        for i in range(len(nums)):
            cur = nums[i]
            if cur in hashset:
                return True
            hashset.add(cur)
        return False





