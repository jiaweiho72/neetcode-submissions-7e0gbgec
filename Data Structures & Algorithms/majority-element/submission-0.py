class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Return the majority element

        idea
        - count every element

        """
        n = len(nums)
        half_count = n / 2

        count = {}
        for i in range(n):
            num = nums[i]
            count[num] = count.get(num, 0) + 1
            if count[num] > half_count:
                return num
        return -1




