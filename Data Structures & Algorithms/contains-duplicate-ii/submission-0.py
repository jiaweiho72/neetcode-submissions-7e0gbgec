class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Same as contains duplicate but index difference <= k

        idea
        - original: set. check if existed in set
        - new: dict. value is the latest occurence of the num
        """

        n = len(nums)
        last_occur_dict = {}
        for i in range(n):
            num = nums[i]
            if num in last_occur_dict:
                if abs(i - last_occur_dict[num]) <= k:
                    return True

            # update last occurence (replace) no matter what
            last_occur_dict[num] = i
        
        return False # False until proven true
