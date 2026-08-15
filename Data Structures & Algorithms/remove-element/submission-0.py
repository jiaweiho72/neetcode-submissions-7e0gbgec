class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        1) change the array nums inplace, removing all occurence of val. flush to the left
        2) return k, the no of elements remaining

        idea
        - a write and read two pointer overwrite
        """
        n = len(nums)
        write_index = 0
        for read_index in range(n):
            cur_num = nums[read_index]
            if cur_num == val: # simulate deleting (by not inserting to write)
                continue
            else:
                nums[write_index] = cur_num
                write_index += 1
        
        return write_index