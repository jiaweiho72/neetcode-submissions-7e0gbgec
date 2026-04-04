class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        4 apr 2026
        notes
        - sorted non-decreasing
        - return: [index1, index2] 1 indexed
        - only one valid solution
        - O(1) space


        1) two pointer 
        - already sorted so it is ok, still O(n)

        2) complement dict method
        """

        n = len(numbers)
        l, r = 0, n - 1

        while l < r: # not equals as l cannot be r in this question
            cur_sum = numbers[l] + numbers[r]
            if cur_sum == target:
                return [l + 1, r + 1]
            elif cur_sum < target:
                # need to make sum bigger -> increase left side
                l += 1
            else:
                r -= 1
        
        return None




