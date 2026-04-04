class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        3 Apr 2026

        - brute force
            - O(n^2) for every element you iterate the whole list and get product

        - optimal O(2n)
            - prefix and postfix
                - on postfix iteration, could just get the product directly
            - get at every index
            - 
        """

        n = len(nums)

        # prefix product
        prefix = [0] * n
        cur_prefix = 1
        for i in range(n):
            cur = nums[i]
            prefix[i] = cur_prefix 
            
            # to not include product of current i number -> update after
            cur_prefix *= cur
        
        # postfix product but just get the result directly instead of having to do another loop
        result = [0] * n
        cur_postfix = 1
        for i in range(n-1, -1, -1):
            cur = nums[i]
            result[i] = prefix[i] * cur_postfix
            
            # update after
            cur_postfix *= cur

        return result




