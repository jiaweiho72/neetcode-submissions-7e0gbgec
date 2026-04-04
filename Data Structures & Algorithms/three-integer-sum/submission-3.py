class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        notes
        - return all triplets: [[num1, num2, num3], ...]

        solution
        - for each index
            - work on the subarray after this index
            - do a two sum on this sub array to find the target
        - to prevent duplicates
            - for sorted, you have to continue while value is the same
        """

        n = len(nums)
        nums.sort()
        target = 0
        triplets = []

        for i in range(n):
            # check for duplicate -> skip
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            cur = nums[i]
            complement = target - cur
            l, r = i + 1, n - 1
            while l < r:
                # wrong - misses the case where you can have  same number
                # # skip duplicates
                # while l < r and nums[l] == nums[l + 1]:
                #     l += 1
                # while l < r and nums[r] == nums[r - 1]:
                #     r -= 1
                
                cur_sum = nums[l] + nums[r]
                if cur_sum == complement:
                    triplets.append([cur, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                        # the right will naturally clean itself
                    l += 1
                elif cur_sum < complement:
                    l += 1
                else:
                    r -= 1
            print(nums[i])
        
        return triplets
            






