class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Bruteforce
        - try every n starting index and each try goes through the whole n list
        Greedy O(n)
        - if current sum of (gas - cost) is negative -> obviously not enough gas, impossible -> can't be starting point
        - else let it be the result and continue moving forward
            - if total diff is negative again 
                means the path from the previous start and the current, none in between can be the start index
                -> need to reset start point as new index
                - but why? gain[A] + gain[B] + gain[C] < 0
                    if B did not fail and it failed at C, C is worse than B and B can't be the start and make it through C
        """
        # 1) Check if valid
        if sum(gas) < sum(cost):
            return -1

        total = 0
        result = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0: # negative -> currently not enough gas to reach next
                total = 0
                result = i + 1

        return result