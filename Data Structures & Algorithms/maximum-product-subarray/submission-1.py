class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Brute-force:
        - O(n^2) - for each num check every possible subarray
        Trying to understand:
                    2           3
                3           -2
            -2          4
        4
        
        Idea: Dynamic Programming, Bottom-up
        - DP as there is repeat calculation as seen above
        - At each index of nums:
            1) keep track of the max
            2) Keep track of the min - for use for negative numbers later
            it is comparing between:
                - cur * min
                - cur * max
                - cur

        - careful, the max must represent products of items that are contiguous up 
        to the index
        - by mutliplying each time to the cur num it ensures that the max/min is wrt to the cur
        num and it is contiguous and there is no gap

        Example:
        [-1,2,-2,3,4,5,-1,9,6,3]



        Time is O(n), space 
        * use temp variable as you are changing cur_max but still need to use the original
        cur_max value for cur_min
        """

        n = len(nums)
        max_product = float('-inf')
        cur_max, cur_min = 1, 1

        for i in range(n - 1, -1, -1):
            num = nums[i]
            """
            For cur_max
            1) num * cur_max if n is positive
            2) num * cur_min if n is negative
            3) num if cur_max/cur_min is bad

            For 3), it handles where the number is zero. If previous num is zero,
            it will start afresh and use num as the max/min
            """
            """
            use temp variable as you are changing cur_max but still need to use the original
            cur_max value for cur_min
            """
            temp_max = cur_max
            cur_max = max(num * cur_max, num * cur_min, num) 
            cur_min = min(num * temp_max, num * cur_min, num)
            max_product = max(max_product, cur_max)

        return max_product

        """
        25 July 2026
        - find subarray with largest product and return the PRODUCT
        note: [x] product is x
        note: A subarray is a contiguous non-empty sequence of elements within an array.
        note: there are negative numbers


        Idea
        - keep track of the maxproduct
        - not exactly a sliding window as there is no constraint on the window size and you are just trying to search all possible sizes
        - brute force
            - go through every element
                - from that element, try all possible subarrays
        - repeated sub problem -> DP
            - at an index, you would be able to know the index onwards max product
            - since it is negative
                - you need to keep track of negative and positive product as  -10*-10 = 100
            - cases of max
                - cur * max
                - cur * min
                - cur
                    - don't continue the array downwards

        mistake: the subarray with max may not start at 0
            - so constantly update the max
            - max variable also need to be float('-inf') due to negative numbers
        
        Time O(n)
        Space O(n)
        """
        from functools import cache
        n = len(nums)
        
        max_prd = float('-inf')

        @cache
        def dfs(i): # return the min and max
            nonlocal max_prd
            # base case
            if i >= n:
                return 1, 1

            cur = nums[i]
            prev_min, prev_max = dfs(i + 1)

            cur_min = min(cur * prev_min, cur, cur * prev_max)
            cur_max = max(cur * prev_min, cur, cur * prev_max)
            max_prd = max(max_prd, cur_max)
            return cur_min, cur_max
        
        dfs(0)
        return max_prd
