class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1 oct 2026
        - sort is nlogn
        - better to use hashmap and check complement

        return the index
        """

        n = len(nums)
        hash_map = {}
        for i in range(n):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]

            hash_map[nums[i]] = i
        
        return -1 # guaranteed valid though





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

