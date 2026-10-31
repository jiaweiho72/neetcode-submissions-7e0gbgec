class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        return all triplets

        sort
        - main two pointer check
        - duplicates
            skip if the num is the same

        no binary search?
        - 

        mistake: you skipped l for every case
        - issue is that you can still use duplicate elements at diff index in new levels    
            - like l and r can be same element. but you don't want to process l on duplicates
        - you just don't want to try the duplicate elements within the same row
        - solution:
            - only skip within the same level, when you found a triplet
        """
        # return [1]

        n = len(nums)
        nums.sort()
        triplets = []
        target = 0
        
        for i in range(n): # choose different starting first element
            l, r = i + 1, n - 1
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            while l < r: # not equals as can't use same element

                cur_sum = nums[i] + nums[l] + nums[r]
                if target == cur_sum:
                    triplets.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                elif target < cur_sum: # need to make smaller -> move left
                    r -= 1
                else:
                    l += 1
                
                

        return triplets
                


        """
        notes
        - return all triplets: [[num1, num2, num3], ...]

        solution
        - for each index
            - work on the subarray after this index
            - do a two sum on this sub array to find the target
        - to prevent duplicates
            - for sorted, you have to continue while value is the same

        Time: O(n^2)
        Space: O(1)
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
            






