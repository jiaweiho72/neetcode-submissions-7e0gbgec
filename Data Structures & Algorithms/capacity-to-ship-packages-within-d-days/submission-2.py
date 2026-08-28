class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        29 Aug 2026 Zouk
        - one day, load as many weights
        - complete all weights which 'days'
        - weights processed in order
        - single day weight can't exceed capacity
        find LEAST weight capacity to at least complete by 'days'

        no greedy solution
        bruteforce search all possible values of capacity

        optimal - binary search
        - search all possible values from 0 to sum(weights)
            - worst case all need in one day
            - binary search is still good, will quickly halve the data
        """

        n = len(weights)
        l, r = 0, sum(weights)
        min_capacity = float('inf')

        while l <= r: # search min possible capacity
            capacity = (l + r) // 2
            capacity_left = capacity
            no_of_days = 1
            
            for i in range(n):
                weight = weights[i]
                # just check if there are any invalid weights
                if weight > capacity: # impossible to ship -> this capacity cannot -> need to increase
                    no_of_days = float('inf') # too many days -> invalid -> try increase capacity
                    break


                if weight <= capacity_left: # still available to use
                    capacity_left -= weight
                else: # need to start a new day
                    capacity_left = capacity
                    capacity_left -= weight
                    no_of_days += 1

            
            if no_of_days <= days: # valid capacity -> try to see if got more optimal -> decrease further
                min_capacity = min(min_capacity, capacity) # log min
                r = capacity - 1
            else: # invalid -> need increase capcity
                l = capacity + 1
        
        return min_capacity


            









