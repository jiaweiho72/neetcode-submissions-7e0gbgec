class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        22 July

        Nsum
        - the outer loops 
        - only base is the twosum
        - can't have iteration as n nested loop not multiple loops side by side
        - recursion (nums, target, k, start)
            - sub case is split by passing down the complement at the next target
                - similar to 3sum, main loop goes through every element and the underneat loop only process to the right of this element
                    - because previous iterations would have covered the left cases
            - base case -> k == 2 -> two sum
                - do two sum for this target starting at this point
                - don
            - else
                iterate through the rest of the list (like the main outer loop in 3 sum)
                    - dfs for every one
            so basically only teh base twosum will do the pointers
        """

        n = len(nums)
        nums.sort()
        result = []
        combination = []

        def nsum(target, k, start):
            nonlocal n
            if start >= n: # out of bounds
                return
            if k == 2: # twosum
                l, r = start, n - 1
                while l < r:
                    cur_sum = nums[l] + nums[r]
                    if cur_sum == target:
                        combination.append(nums[l])
                        combination.append(nums[r])
                        result.append(combination.copy())

                        combination.pop()
                        combination.pop()

                        l += 1
                        r -= 1
                        while l < r and nums[l - 1] == nums[l]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif cur_sum < target:
                        l += 1
                    else:
                        r -= 1
                return
                
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]: # skip main loop duplicate
                    continue
                complement = target - nums[i]

                combination.append(nums[i])
                nsum(complement, k - 1, i + 1)
                combination.pop()
        nsum(target, 4, 0)
        return result
            















        """
        Base case - 2Sum
        
        Idea: Recursion
        - kSum
            - parameters: nums, target, k, start
            - if base case -> twoSum
        note: target is remainder

        """
        def kSum(nums, target, k, start):
            res = []
            n = len(nums)

            # Base case: TwoSum (sorted)
            if k == 2:
                l, r = start, n - 1
                while l < r: # not == as cannot use same element
                    cur = nums[l] + nums[r]
                    if cur == target:
                        res.append([nums[l], nums[r]])

                        # Handle duplicate (both left and right)
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        
                        l += 1
                        r -= 1
                    
                    elif cur < target: # need to increase -> increase l
                        l += 1
                    else:
                        r -= 1

            else:
                # Reduce k to k-1
                for i in range(start, n - k + 1): # just to end early -> give space for other k
                    # Skip duplicates - same as prev value
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    # Early termination
                    if nums[i] * k > target or nums[-1] * k < target:
                        break
                    
                    for subset in kSum(nums, target - nums[i], k - 1, i + 1):
                        res.append([nums[i]] + subset)
            return res

        nums.sort()
        return kSum(nums, target, 4, 0)